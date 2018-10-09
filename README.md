# addlicense 

*addlicense* is a simple utility that automatically inserts a specified license file or copyright message at the top of one or more source code files

```
usage: addlicense.py [-h] [--licensefile LICENSEFILE]
                     [--commentblock COMMENTBLOCK] [--comment COMMENT] [-s]
                     [--backup]
                     sourcefiles [sourcefiles ...]

Automatically inserts a specified license file or copyright message at the top
of one or more source code files

positional arguments:
  sourcefiles           a list of files to update with the license or
                        copyright message

optional arguments:
  -h, --help            show this help message and exit
  --licensefile LICENSEFILE
                        a file containing the license or copyright text,
                        defaulting to LICENSE.txt
  --commentblock COMMENTBLOCK
                        a space-separated string indicating the characters to
                        use at the beginning and end of the license message to
                        demark them as a comment block
  --comment COMMENT     a string indicating the characters to use at the
                        beginning of each line of the license message to
                        demark them as comments
  -s, --skip-shebang-executable
                        skip the initial shebang executable command: if the
                        source file starts with a comment symbol (identified
                        via the --comment option) followed by a shebang, to
                        indicate an executable script on a POSIX system, then
                        the license text will be inserted AFTER this initial
                        line
  --backup              keep a copy of the original source-file with a .bak
                        extension


```

## Installation

*addlicense* is written in Python, and you can use the pip installer to install it thus:
```
$ pip install addlicense
```
## Homepage

You can find the homepage of *addlicense* at https://github.com/hossg/addlicense
