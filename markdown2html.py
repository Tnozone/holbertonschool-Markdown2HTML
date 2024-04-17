#!/usr/bin/python3
"""
Write a script markdown2html.py that takes two string arguments:

    First argument is the name of the Markdown file
    Second argument is the output file name
"""
import sys
import os
import re
import hashlib

def heading(line):
    ''' Parse and convert Markdown headings to HTML '''
    heading_num = len(line) - len(line.lstrip('#'))
    if 1 <= heading_num <= 6:
        return f'<h{heading_num}>{line.lstrip("#").strip()}</h{heading_num}>\n'
    return line

def unordered_list(line, in_list=False):
    ''' Parse and convert Markdown unordered lists to HTML '''
    if line.lstrip().startswith('-'):
        list_item = f'<li>{line.lstrip("-").strip()}</li>\n'
        if not in_list:
            return f'<ul>\n{list_item}', True
        else:
            return list_item, in_list
    elif in_list:
        return '</ul>\n' + line, False
    else:
        return line, in_list

def ordered_list(line):
    ''' Parse and convert Markdown ordered lists to HTML '''
    if line.lstrip().startswith('1.'):
        list_item = f'<li>{line.lstrip("1.").strip()}</li>\n'
        return f'<ol>\n{list_item}</ol>'
    return line

def convert_markdown_to_html(markdown_file, html_file):
    in_list = False  # Initialize the in_list variable
    with open(markdown_file) as md, open(html_file, 'w') as html:
        for line in md:
            line, in_list = unordered_list(line, in_list)
            line = heading(line)
            line = ordered_list(line)
            html.write(line)

def check_arguments():
    ''' Check command line arguments '''
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    check_arguments()
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)
    