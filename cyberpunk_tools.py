import sys
from random import randint

VERSION = "0.0.4"

# =================================================================

def print_help():
    print("Usage:\n  cyberpunk_tools <option>")
    print("Options:")
    print("  -h, --help: display this help message")
    print("  -v, --version: display the current version")
    print("  character <option>: character related tools")

def print_character_help():
    print("Usage:\n  cyberpunk_tools character <option>")
    print("Options:")
    print("  -h, --help: display this help message")
    print("  sgs: gen a random sgs")

def print_version():
    print(f"cyberpunk tools version: {VERSION}")

def gen_sgs()->str:
    sex_roll=randint(1,100)
    sex=""
    if sex_roll <= 49:
        sex="M"
    elif sex_roll <= 98:
        sex="F"
    else:
        sex_roll=randint(1,100)
        if sex_roll <= 45:
            sex="IM"
        elif sex_roll <= 90:
            sex="IF"
        else:
            sex="IA"

    gender_roll=randint(1,100)
    gender=""
    if gender_roll <= 95:
        gender=sex[-1]
    else:
        gender_roll=randint(1,100)
        if gender_roll <= 95:
            gender="M" if sex[-1]=="F" else "F"
        elif gender_roll <= 99:
            gender="NB"
        else:
            gender="GF"

    sexuality_roll=randint(1,100)
    sexuality=""
    if sexuality_roll <= 95:
        sexuality="Hete"
    else:
        sexuality_roll=randint(1,100)
        if sexuality_roll <= 60:
            sexuality="Homo"
        elif sexuality_roll <= 90:
            sexuality="Bi"
        elif sexuality_roll <= 95:
            sexuality="A"
        else:
            sexuality="Pan"
    return f"{sex}/{gender}/{sexuality}"

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
    if arg in ["character"]:
        if len(args)<2:
            print("No options provided...", file=sys.stderr)
            print_help()
            sys.exit(1)
        arg=args[1]
        if arg in ["-h", "--help"]:
            print_character_help()
            sys.exit(0)
        if arg in ["sgs"]:
            print(gen_sgs())
            sys.exit(0)


    print(f"Unknown option: {arg}",file=sys.stderr)
    print_help()
    sys.exit(2)



