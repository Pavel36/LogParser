import sys
import os


def reader():
    if os.path.exists(sys.argv[1]):
        if os.path.isfile(sys.argv[1]):
            if os.path.splitext(sys.argv[1])[1] == '.log':
                f = open(sys.argv[1], 'r')
                for line in f:
                    print(line)
        elif os.path.isdir(sys.argv[1]):
            for file in os.listdir(sys.argv[1]):
                if os.path.splitext(file)[1] == '.log':
                    print('filename=', file)
                    f = open(sys.argv[1] + '\\' + file, 'r')
                    for line in f:
                        print(line)
                    f.close()

    else:
        print('file not found')


reader()

# f = open(sys.argv[1], 'r')
# for line in f:
#     print(line)
