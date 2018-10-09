#!python3
#     addlicense automatically inserts a specified license file or copyright message at the top of one or more source code files
# 
#     Copyright (C) 2018  Hossein Ghodse
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
# 
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.



import argparse
import shutil
def main():
    print()
    parser = argparse.ArgumentParser(description='Automatically inserts a specified license file or copyright message at ' \
                                                'the top of one or more source code files',
                                     epilog='More information: https://github.com/hossg/addlicense')
    parser.add_argument('--licensefile', default="LICENSE_NOTICE.txt",
                        help='a file containing the license or copyright text, defaulting to LICENSE_NOTICE.txt')
    parser.add_argument('--commentblock',
                        help='a space-separated string indicating the characters to use at the beginning and end of the ' \
                        'license message to demark them as a comment block')
    parser.add_argument('--comment',
                        help='a string indicating the characters to use at the beginning of each line of the  ' \
                        'license message to demark them as comments')
    parser.add_argument('-s','--skip-shebang-executable', action='store_true',
                        help='skip the initial shebang executable command: if the source file starts with a comment symbol '\
                        '(identified via the --comment option) ' \
                        'followed by a shebang, to indicate an executable script on a POSIX system, then the license ' \
                        'text will be inserted AFTER this initial line')
    parser.add_argument('--backup', action="store_true",
                        help='keep a copy of the original source-file with a .bak extension')
    parser.add_argument('sourcefiles', nargs='+',
                        help='a list of files to update with the license or copyright message')


    args = parser.parse_args()

    comment=''
    if(args.comment):
        comment=args.comment + ' '
    if(args.commentblock):
        (opencomment,closecomment)=args.commentblock.split()
    licensetext=[]
    with open(args.licensefile,'r') as f:
        licensetext_lines=f.readlines()
        for line in licensetext_lines:
            line = comment + line
            licensetext.append(line)
        licensetext.append('\n\n')

    for filename in args.sourcefiles:

        print('Processing {}'.format(filename))
        if args.backup:
            dest=filename+'.bak'
            shutil.copyfile(filename, dest)

        with open(filename,'r') as f:
            lines = f.readlines()
            #text = licensetext + '\n\n' + f.read()

        with open(filename,'w') as f:
            if args.skip_shebang_executable:
                if lines[0].startswith(args.comment+'!'):
                    f.write(lines[0])
                    lines=lines[1:] # remove the first line, having now written it

            if(args.commentblock):
                f.writelines(opencomment+'\n')
            f.writelines(licensetext)
            if (args.commentblock):
                f.writelines(closecomment+'\n')
            f.writelines(lines)

    print("\nDone!")

