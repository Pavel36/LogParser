import sys
import os
import re
from tqdm import tqdm


def reader(filename, pattern, allow_ext):
    if os.path.exists(filename):
        with open(filename + '\\out.txt', 'w') as out:
            if os.path.isfile(filename):
                if re.search(allow_ext, os.path.splitext(filename)[1]):
                    f = open(filename, 'r')
                    for line in tqdm(f.readlines(), desc=filename):
                        if re.search(pattern, line):
                            out.write(line)
                    f.close()
            elif os.path.isdir(filename):
                for file in os.listdir(filename):
                    if os.path.splitext(file)[1] == '.log':
                        out.write('filename: ' + file + '\n')
                        f = open(filename + '\\' + file, 'r')
                        for line in tqdm(f.readlines(), desc=file):
                            if re.search(pattern, line):
                                out.write(line)
                        f.close()
        out.close()
    else:
        print('file not found')


# reader("D:\Logs", "VERBOSE", '.log')

if len(sys.argv) == 4:
    reader(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print('wrong number of arguments')

# py Parser.py D:\Logs Error: .log
