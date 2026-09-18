import sys

VERSION = "0.0.1"

# =================================================================

def print_help():
    print("Usage:\n  cyberpunk_tools <option>")
    print("Options:")
    print("  -h, --help: display this help message")
    print("  -v, --version: display the current version")

def print_version():
    print(f"cyberpunk tools version: {VERSION}")

# =================================================================

if __name__ == '__main__':

    args=sys.argv[1:]

    if len(args) < 1:
        print("No options provided...",file=sys.stderr)
        print_help()
        sys.exit(1)

    arg=args[0]

    if arg in ["-v", "--version"]:
        print_version()
        sys.exit(0)
    if arg in ["-h", "--help"]:
        print_help()
        sys.exit(0)

    print(f"Unknown option: {arg}",file=sys.stderr)
    print_help()
    sys.exit(2)



