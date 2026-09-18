import sys

def print_help():
    print("Usage: python cyberpunk_tools.py [options]")
    print("Options:")
    print("  -h, --help: display this help message")
    print("  -v, --version: display the current version")

def print_version():
    print(f"cyberpunk tools version: {VERSION}")
# =================================================================
VERSION = "0.0.1"
# =================================================================
if __name__ == '__main__':
    args=sys.argv[1:]
    if len(args) < 1:
        print_help()
        exit(1)
    if args[0] == "-v" or args[0] == "--version":
        print_version()
        exit(0)

    print_help()
    exit(2)



