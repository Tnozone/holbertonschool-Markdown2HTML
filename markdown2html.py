#!/usr/bin/python3
"""
Write a script markdown2html.py that takes two string arguments:

    First argument is the name of the Markdown file
    Second argument is the output file name
"""
import sys
import os

def convert_markdown_to_html(markdown_file, html_file):
    with open(markdown_file) as md, open(html_file, 'w') as html:
        for line in md:
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
