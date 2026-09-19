import sys
from enum import IntEnum
from random import randint,choice

VERSION = "0.0.6"
class EXIT_CODES(IntEnum):
    OK = 0
    NO_OPTION_FOUND = 1
    OPTION_NOT_RECOGNIZED = 2
    MODE_NOT_RECOGNIZED = 3 # Stat gen mode not recognized

# =================================================================

def print_help():
    """
    Print help message to stdout
    :return:
    """
    print("Usage:\n  cyberpunk_tools <option>")
    print("Options:")
    print("  -h, --help: display this help message")
    print("  -v, --version: display the current version")
    print("  character <option>: character related tools")
    print("    -h, --help: display this help message")
    print("    sgs: gen a random sgs string")
    print("    role: gen a random role string")
    print("    stats <mode>: gen random stats following a given mode")
    print("      9d10:  roll 9d10 and return the CP for the user to distribute")
    print("      d10:   roll d10 for every stat, min 3")

def print_character_help():
    """
    Print help message of character option to stdout
    :return:
    """

    print("Usage:\n  cyberpunk_tools character <option>")
    print("Options:")
    print("  -h, --help: display this help message")
    print("  sgs: gen a random sgs string")
    print("  role: gen a random role string")
    print("  stats <mode>: gen random stats following a given mode")
    print("    9d10:  roll 9d10 and return the CP for the user to distribute")
    print("    d10:   roll d10 for every stat, min 3")


def print_version():
    """
    Print version message to stdout
    :return:
    """

    print(f"cyberpunk tools version: {VERSION}")

def gen_sgs()->str:
    """
    Generate a random sex, gender and sexuality string

    Format: s/g/s

    Possible values:
        sex:
            - M - Male
            - F - Female
            - IF - Intersex Female Appearance
            - IM - Intersex Male Appearance
            - IA - Intersex Androgynous Appearance
        gender:
            - M - Male
            - F - Female
            - NB - Non binary
            - GF - Gender Fluid
        sexuality:
            - Hete - Heterosexual
            - Homo - Homosexual
            - Bi - Bisexual
            - A - Asexual
            - Pan - Pansexual


    :return:formatted string
    """
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
        if gender_roll <= 95 and sex[-1]!="A":
            gender = "M" if sex[-1] == "F" else gender
            gender = "F" if sex[-1] == "M" else gender
        elif gender_roll <= 99:
            gender="NB"
        else:
            gender="GF"

    sexuality_roll=randint(1,100)
    sexuality=""
    if sexuality_roll <= 95 and gender!="A":
        sexuality="Hete"
    else:
        sexuality_roll=randint(1,100)
        if sexuality_roll <= 60 and sex[-1]!="A":
            sexuality="Homo"
        elif sexuality_roll <= 90:
            sexuality="Bi"
        elif sexuality_roll <= 95:
            sexuality="A"
        else:
            sexuality="Pan"
    return f"{sex}/{gender}/{sexuality}"

def gen_role()->str:
    """
    Generate a random role string

    Possible values:
        - Rockerboy
        - Solo
        - Netrunner
        - Corporate
        - Techie
        - Cop
        - Fixer
        - Media
        - Nomad
        - Medtech(tech esp)
    :return:
    """
    roles=[
        "Rockerboy",
        "Solo",
        "Netrunner",
        "Corporate",
        "Techie",
        "Cop",
        "Fixer",
        "Media",
        "Nomad",
        "Medtech(tech esp)",
    ]
    return  choice(roles)

def gen_stats(mode,show=False)->dict:
    """
    Generate a random stats dict
    :param mode:
      9d10: Returns CP to distribute between stats by the user
      d10: Returns stats (3-10)
    :return:
    """

    match mode:
        case "9d10":
            stats=gen_stats_9d10()
            if show:
                print(f"CP to distribute between stats: {stats["CP"]}")
            return stats
        case "d10":
            stats=gen_stats_d10()
            if show:
                print(f"Stats:")
                for k in stats:
                    print(f"{k:<4}: {stats[k]:2}")
            return stats
        case _:
            print(f"Unknown mode: {mode}", file=sys.stderr)
            print_help()
            sys.exit(EXIT_CODES.MODE_NOT_RECOGNIZED)

def gen_stats_9d10()->dict:
    acc=0
    for i in range(9):
        acc+=randint(1,10)
    return {"CP":acc}

def gen_stats_d10()->dict:
    stats = {
        "int": 0,
        "ref": 0,
        "tech": 0,
        "cool": 0,
        "attr": 0,
        "luck": 0,
        "mov": 0,
        "body": 0,
        "emp": 0
    }
    for k in stats:
        stats[k]=randint(3,10)
    return stats

# =================================================================




if __name__ == '__main__':

    # ignore exec path
    args=sys.argv[1:]

    if len(args) < 1:
        print("No options provided...",file=sys.stderr)
        print_help()
        sys.exit(EXIT_CODES.NO_OPTION_FOUND)

    arg=args[0]

    if arg in ["-v", "--version"]:
        print_version()
        sys.exit(EXIT_CODES.OK)
    if arg in ["-h", "--help"]:
        print_help()
        sys.exit(EXIT_CODES.OK)
    if arg in ["character"]:
        if len(args)<2:
            print("No options provided...", file=sys.stderr)
            print_help()
            sys.exit(EXIT_CODES.NO_OPTION_FOUND)
        arg=args[1]
        if arg in ["-h", "--help"]:
            print_character_help()
            sys.exit(EXIT_CODES.OK)
        if arg in ["sgs"]:
            print(gen_sgs())
            sys.exit(EXIT_CODES.OK)
        if arg in ["role"]:
            print(gen_role())
            sys.exit(EXIT_CODES.OK)
        if arg in ["stats"]:
            if len(args)<2:
                print("No option provided...", file=sys.stderr)
                print_help()
                sys.exit(EXIT_CODES.NO_OPTION_FOUND)
            mode=args[2]
            gen_stats(mode,show=True)
            sys.exit(EXIT_CODES.OK)


    print(f"Unknown option: {arg}",file=sys.stderr)
    print_help()
    sys.exit(EXIT_CODES.OPTION_NOT_RECOGNIZED)



