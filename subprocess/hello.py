import sys


def main():
    """
    Get the name from the command line, using 'World' as a fallback.
    """

    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'World'
    print('Hello', name)


if __name__ == '__main__':
    main()
