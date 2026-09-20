import sys
from enum import IntEnum
from random import randint,choice
from unittest import case

VERSION = "0.0.8"
class ExitCodes(IntEnum):
    OK = 0
    NO_OPTION_FOUND = 1
    OPTION_NOT_RECOGNIZED = 2
    MODE_NOT_RECOGNIZED = 3 # Stat gen mode not recognized
    WRONG_DATA_TYPE = 4
    INVALID_DATA = 5
    UNEXPECTED_ERROR = 6

# ======================================================================================================================

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
    print("    life [age]: generates life events for given age")
    print("                age must be an integer > 0")
    print("                age option defaults to random ( 2d6 + 16 )")

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

    9d10: Returns CP to distribute between stats by the user

    d10: Returns stats (3-10)

    :param mode:str - 9d10 | d10
    :param show:bool - whether to print the output to stdout

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
            sys.exit(ExitCodes.MODE_NOT_RECOGNIZED)

def gen_stats_9d10()->dict:
    acc=0
    for i in range(9):
        acc+=randint(1,10)
    return {"CP":acc}

def gen_lucky_event(show=False)->str:
    roll = randint(1, 10)
    event = ""

    match roll:
        case 1:
            event = "powerful connection : "
            roll = randint(1, 10)

            if roll <= 4:
                event += "in police dept"
            elif roll <= 7:
                event += "in District Attorney's office"
            elif roll <= 10:
                event += "in mayor's office"
        case 2:
            event = f"financial windfall : +{randint(1,10)*100}ed"
        case 3:
            event = f"big score : +{randint(1,10)*100}ed"
        case 4:
            event = "find sensei : begin at +2 or add +1 to martial skill"
        case 5:
            event = "find teacher : begin at +2 or add +1 to int skill"
        case 6:
            event = "powerful corpo exec owes you one"
        case 7:
            event = "friends with local nomad pack. eq -> family +2"
        case 8:
            event = "friend popo. eq -> streetwise +2"
        case 9:
            event = "local boostergang likes you. eq -> family +2 beware"
        case 10:
            event = "find combat teacher : begin at +2 or add +1 to weapon skill, no ma/brawling"

    if show:
        print(event)
    return event

def gen_disaster_event(show=False)->str:
    roll = randint(1,10)
    event = ""

    match roll:
        case 1:
            event = f"financial loss/debt : -{randint(1,10)*100}ed"
        case 2:
            event = f"prison :{randint(1,10)} months"
        case 3:
            event = "illness/addiction : -1 REF"
        case 4:
            event = f"betrayal : "
            roll = randint(1,10)
            if roll <=3:
                event += "blackmail"
            elif roll <=7:
                event += "secret exposed"
            else:
                event += "betrayed by romance/career partner"
        case 5:
            event = "accident : "
            roll = randint(1,10)
            if roll <=4:
                event += "disfigured : -5 ATTR"
            elif roll <=6:
                event += f"hospital : {randint(1,10)} months"
            elif roll <=8:
                event += f"mem loss : {randint(1,10)} months"
            else:
                event += f"recurrent nightmares : 80% chance"
        case 6:
            event = "close one killed : "
            roll = randint(1,3)

            if roll == 1:event += "lover : "
            elif roll == 2:event += "friend : "
            elif roll == 3:event += "relative : "

            roll = randint(1,10)
            if roll <=5:
                event += "accident"
            elif roll <=8:
                event += "murdered : unknown"
            else:
                event += "murdered : known"
        case 7:
            event = "false accusation : "
            roll = randint(1,10)

            if roll <=3:
                event += "theft"
            elif roll <=5:
                event += "cowardice"
            elif roll <=8:
                event += "murder"
            elif roll <=9:
                event += "rape"
            elif roll <=10:
                event += "lying/betrayal"
        case 8:
            event = "hunted by law : "
            roll = randint(1,10)

            if roll <=3:
                event += "couple local cops"
            elif roll <=6:
                event += "entire local force"
            elif roll <=8:
                event += "state police/militia"
            elif roll <=10:
                event += "national police force"
        case 9:
            event = "hunted by corpo : "
            roll = randint(1,10)

            if roll <=3:
                event += "small local firm"
            elif roll <=6:
                event += "larger corp state wide"
            elif roll <=8:
                event += "big national corp, nation wide"
            elif roll <=10:
                event += "mega corp, multinational"
        case 10:
            event = "mental/physical incapacitation : "
            roll = randint(1,10)
            if roll <=3:
                event += "-1 REF"
            elif roll <=7:
                event += "-1 COOL"
            elif roll <=10:
                event += "-1 COOL & -1 REF"

    if  show:
        print(event)
    return event

def gen_big_prob_big_wins(show=False)->str:
    roll=randint(1,2)
    if roll==1:
        event = f"disaster event : {gen_disaster_event()}"
        if show:
            print(event)
        return event
    elif roll==2:
        event = f"lucky event : {gen_lucky_event()}"
        if show:
            print(event)
        return event
    else:
        print(f"d2 returned {roll} O.o ...",file=sys.stderr)
        sys.exit(ExitCodes.UNEXPECTED_ERROR)

def gen_made_friend(show=False)->str:
    roll=randint(1,10)
    event=""
    match roll:
        case 1:
            event += "like bro/sis"
        case 2:
            event += "like kid bro/sis"
        case 3:
            event += "teacher/mentor"
        case 4:
            event += "partner/co-worker"
        case 5:
            event += "old lover"
        case 6:
            event += "old enemy"
        case 7:
            event += "like foster parent"
        case 8:
            event += "relative"
        case 9:
            event += "old childhood friend"
        case 10:
            event += "met through common interest"

    if show:
        print(event)
    return event

def gen_made_enemy(show=False)->str:
    roll = randint(1, 10)
    event = ""
    match roll:
        case 1:
            event += "ex friend"
        case 2:
            event += "ex lover"
        case 3:
            event += "relative"
        case 4:
            event += "childhood enemy"
        case 5:
            event += "working for you"
        case 6:
            event += "you work for them"
        case 7:
            event += "partner or co-worker"
        case 8:
            event += "booster gang member"
        case 9:
            event += "corpo exec"
        case 10:
            event += "gov official"

    # the cause
    roll = randint(1, 10)
    match roll:
        case 1:
            event += " : caused the other to lose face or status"
        case 2:
            event += " : caused the loss of a lover, friend or relative"
        case 3:
            event += " : caused a major humiliation"
        case 4:
            event += " : accused the other of cowardice or other personal flaw"
        case 5:
            event += " : caused a physical disability : "
            roll = randint(1, 6)
            if roll <= 2: event += "lose eye"
            elif roll <= 4: event += "lose arm"
            elif roll <= 6: event += "badly scarred"
        case 6:
            event += " : deserted/betrayed the other "
        case 7:
            event += " : turned down other's job / romantic offer"
        case 8:
            event += " : you just didn't like each other"
        case 9:
            event += " : was a romantic rival "
        case 10:
            event += " : foiled a plan of the other's"

    # who's fracked off?
    roll = randint(1, 3)
    match roll:
        case 1:
            event += " : they hate you"
        case 2:
            event += " : you hate them"
        case 3:
            event += " : mutual hate"

    #watcha gonna do about it?
    roll = randint(1, 5)
    match roll:
        case 1:
            event += " : muderous/killing rage & kill them"
        case 2:
            event += " : avoid them"
        case 3:
            event += " : backstab them indirectly"
        case 4:
            event += " : ignore them"
        case 5:
            event += " : attack verbally"

    #what can they throw against you?
    roll = randint(1, 10)
    match roll:
        case 1|2|3:
            event += " : himself"
        case 4|5:
            event += " : himself + few friends"
        case 6|7:
            event += " : entire gang"
        case 8|9:
            event += " : small corp"
        case 10:
            event += " : full gov agency"

    if show:
        print(event)
    return event

def gen_frenemies(show=False)->str:
    roll=randint(1,2)
    if roll==1:
        event = f"made friend : {gen_made_friend()}"
        if show:
            print(event)
        return event
    elif roll==2:
        event = f"made enemy : {gen_made_enemy()}"
        if show:
            print(event)
        return event
    else:
        print(f"d2 returned {roll} O.o ...",file=sys.stderr)
        sys.exit(ExitCodes.UNEXPECTED_ERROR)

def gen_romance(show=False)->str:
    roll=randint(1,10)
    event = ""
    match roll:
        case 1|2|3|4:
            event += "happy love affair"
            if show:
                print(event)
            return event
        case 5:
            event += "tragic love affair : "
            roll = randint(1,10)
            match roll:
                case 1:
                    event += "died in accident"
                case 2:
                    event += "mysteriously vanished"
                case 3:
                    event += "didn't work out"
                case 4:
                    event += "personal goal / vendetta came between you"
                case 5:
                    event += "kidnapped"
                case 6:
                    event += "went insane"
                case 7:
                    event += "suicide"
                case 8:
                    event += "killed in a fight"
                case 9:
                    event += "rival cut you of the action"
                case 10:
                    event += "imprisoned or exiled"
        case 6|7:
            event += "love affair with problems : "
            roll = randint(1,10)

            match roll:
                case 1:
                    event += "lover's friends/family hate you"
                case 2:
                    event += "lover's friends/family would use any means to get rid of you"
                case 3:
                    event += "friends/family hate your lover"
                case 4:
                    event += "one of you has a romantic rival"
                case 5:
                    event += "you are separated in some way"
                case 6:
                    event += "you fight constantly"
                case 7:
                    event += "you're professional rivals"
                case 8:
                    event += "one of you is insanely jealous"
                case 9:
                    event += "one of you is 'messing around'"
                case 10:
                    event += "you have conflicting backgrounds and families"
        case 8|9|10:
            event += "fast affairs / hot dates"

    if show:
        print(event)
    return event


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

def gen_life_events(age:int,show=False)->dict:
    if not isinstance(age,int):
        print("Age must be an integer greater than 16...",file=sys.stderr)
        print_help()
        sys.exit(ExitCodes.WRONG_DATA_TYPE)
    if age<=16:
        print("Age must be an integer greater than 16...", file=sys.stderr)
        print_help()
        sys.exit(ExitCodes.WRONG_DATA_TYPE)

    res = {}

    if age <=16:
        if show:
            print("Too young to have registries...")
            return res

    print(f"Age: {age}")
    print("===============================================")
    for year in range(age-16):
        roll=randint(1,6)+randint(1,6)
        date=2020-age+16+year

        if roll <= 3:
            res[year] = f"{date}: Big Prob/big wins : {gen_big_prob_big_wins()}"
        elif roll <= 6:
            res[year] = f"{date}: Frenemies : {gen_frenemies()}"
        elif roll <= 8:
            res[year] = f"{date}: Romance : {gen_romance()}"
        else:
            res[year] = f"{date}: Nothing"

        if show:
            print(res[year])

    return res


# ======================================================================================================================

if __name__ == '__main__':

    # ignore exec path
    args=sys.argv[1:]

    if len(args) < 1:
        print("No options provided...",file=sys.stderr)
        print_help()
        sys.exit(ExitCodes.NO_OPTION_FOUND)

    arg=args[0]

    if arg in ["-v", "--version"]:
        print_version()
        sys.exit(ExitCodes.OK)

    if arg in ["-h", "--help"]:
        print_help()
        sys.exit(ExitCodes.OK)

    if arg in ["character"]:
        if len(args)<2:
            print("No options provided...", file=sys.stderr)
            print_help()
            sys.exit(ExitCodes.NO_OPTION_FOUND)
        arg=args[1]

        if arg in ["sgs"]:
            print(gen_sgs())
            sys.exit(ExitCodes.OK)

        if arg in ["role"]:
            print(gen_role())
            sys.exit(ExitCodes.OK)

        if arg in ["stats"]:
            if len(args)<3:
                print("No mode provided...", file=sys.stderr)
                print_help()
                sys.exit(ExitCodes.NO_OPTION_FOUND)

            mode=args[2]
            gen_stats(mode,show=True)
            sys.exit(ExitCodes.OK)

        if arg in ["life"]:
            if len(args)==3 and args[2].isdigit():
                age=int(args[2])
            elif len(args)==2:
                age=randint(1,6)+randint(1,6)+16
            else:
                print("Age must be an integer greater than 16...", file=sys.stderr)
                print_help()
                sys.exit(ExitCodes.WRONG_DATA_TYPE)

            if age<=16:
                print("Age must be an integer greater than 16...", file=sys.stderr)
                print_help()
                sys.exit(ExitCodes.INVALID_DATA)

            gen_life_events(age,show=True)
            sys.exit(ExitCodes.OK)

    print(f"Unknown option: {arg}",file=sys.stderr)
    print_help()
    sys.exit(ExitCodes.OPTION_NOT_RECOGNIZED)
