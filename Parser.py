import sys
import os
import re
import time
from tqdm import tqdm


def reader(filename, pattern):
    if os.path.exists(filename):
        out = open(filename + '\\out.txt', 'w')
        if os.path.isfile(filename):
            if os.path.splitext(filename)[1] == '.log':
                f = open(filename, 'r')
                for line in f:
                    if re.search(pattern, line):
                        out.write(line)
                f.close()
        elif os.path.isdir(filename):
            for file in tqdm(os.listdir(filename)):
                if os.path.splitext(file)[1] == '.log':
                    out.write('filename: ' + file + '\n')
                    f = open(filename + '\\' + file, 'r')
                    for line in f:
                        if re.search(pattern, line):
                            out.write(line)
                    f.close()
        out.close()
    else:
        print('file not found')


#reader(sys.argv[1], sys.argv[2])
# py Parser.py D:\Logs Error:

reader("D:\Logs", "VERBOSE")
