import sys


def main():
    print('hello world')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))


if __name__ == '__main__':
    main()
