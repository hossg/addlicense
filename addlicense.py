#!/Users/hossein/anaconda3/bin/python3

# addlicense automatically inserts a specified license file or copyright message at the top of one or more source code
# files

import argparse


parser = argparse.ArgumentParser(description='Automatically inserts a specified license file or copyright message at ' \
                                            'the top of one or more source code files')
parser.add_argument('--license-file', default="LICENSE.txt",
                    help='a file containing the license or copyright text, defaulting to LICENSE.txt')
parser.add_argument('--commentblock',
                    help='a space-separated string indicating the characters to use at the beginning and end of the ' \
                    'license message to demark them as a comment block')
parser.add_argument('--comment',
                    help='a string indicating the characters to use at the beginning of each line of the  ' \
                    'license message to demark them as comments')
parser.add_argument('-s','--skip-shebang-executable', action='store_false',
                    help='skip the initial shebang executable command: if the source file starts with a comment symbol '\
                    '(identified via the --comment option) ' \
                    'followed by a shebang, to indicate an executable script on a POSIX system, then the license ' \
                    'text will be inserted AFTER this initial line')
parser.add_argument('--backup',
                    help='keep a copy of the original source-file with a .bak extension')
parser.add_argument('source-files', nargs='+',
                    help='a list of files to update with the license or copyright message')


args = parser.parse_args()
