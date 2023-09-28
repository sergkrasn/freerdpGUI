from src.window import main
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='freerdpgui', usage='%(prog)s [--c]')
    parser.add_argument('config', nargs='*', type=str, default="",
                        help='Input file name with configuration',)
    args = parser.parse_args()
    try:
        main(args.config[0])
    except IndexError:
        main()
