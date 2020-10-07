import sys
import os
import re


def reader(filename, pattern):
    if os.path.exists(filename):
        if os.path.isfile(filename):
            if os.path.splitext(filename)[1] == '.log':
                f = open(filename, 'r')
                for line in f:
                    if re.search(pattern, line):
                        print(line)
                f.close()
        elif os.path.isdir(filename):
            for file in os.listdir(filename):
                if os.path.splitext(file)[1] == '.log':
                    print('filename=', file)
                    f = open(filename + '\\' + file, 'r')
                    for line in f:
                        if re.search(pattern, line):
                            print(line)
                    f.close()
    else:
        print('file not found')


#reader(sys.argv[1], sys.argv[2])
# py Parser.py D:\Logs Error:

reader("D:\Logs", "VERBOSE")
