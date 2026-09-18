import sys

def print_help():
    print("Usage: python cyberpunk_tools.py option")
    print("Options:")
    print("  -h, --help: display this help message")
    print("  -v, --version: display the current version")

def print_version():
    print(f"cyberpunk tools version: {VERSION}")
# =================================================================
VERSION = "0.0.1"
# =================================================================
if __name__ == '__main__':
    if not sys.argv or len(sys.argv) < 2:
        print(f"No options provided...")
        print_help()
        sys.exit(1)

    args=sys.argv[1:]
    arg=args[0]

    if arg in ["-v", "--version"]:
        print_version()
        sys.exit(0)

    print(f"Unknown option: {arg}")
    print_help()
    sys.exit(2)



