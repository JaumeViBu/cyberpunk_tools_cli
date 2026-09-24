# Cyberpunk Tools CLI

A lightweight unofficial fanmade command-line utility for generating random **Cyberpunk 2020** character elements ( stats, roles, life paths, full characters, npcs and more ) for use at the table.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Homebrew%20Content%20Policy-lightgrey)](#legal--disclaimer)

---

## Overview

`cyberpunk_tools` is a small, dependency-free Python CLI that automates a handful of random-generation tasks from the Cyberpunk 2020 Lifepath and character creation rules. It is designed for GMs and players who want to quickly roll up background details or stat arrays without reaching for dice.

The tool uses game mechanics, role names, and Lifepath tables for **automation and summarization only**. It does not reproduce full descriptive text, stat blocks, or rulesets from R. Talsorian Games products.

---

## Requirements

- **Python 3.10 or later** (the script uses `match`/`case` structural pattern matching and `IntEnum`)
- No third-party dependencies

---

## Installation

Clone the repository and run the script directly:

```bash
git clone https://github.com/JaumeViBu/cyberpunk_tools_cli.git
cd cyberpunk_tools_cli
python cyberpunk_tools.py --help
```

On Linux make it executable and drop it on your `PATH`:

```bash
chmod +x cyberpunk_tools.py
ln -s "$PWD/cyberpunk_tools.py" ~/.local/bin/cyberpunk_tools
```

On Windows, in PowerShell:  
```powershell
notepad $PROFILE
```
add:  
```
function cyberpunk_tools {
    python <full path to >\cyberpunk_tools.py $args
}
```
then it can be called in a PowerShell terminal using command
```powershell
cyberpunk_tools
```

---

## Usage

```
cyberpunk_tools <option>
```

### Top-level options

| Option | Description |
| --- | --- |
| `-h`, `--help` | Display the help message |
| `-v`, `--version` | Display the current version |
| `character <option>` | Character-related tools (see below) |

### Character options

```
cyberpunk_tools character <option>
```

| Option | Description |
| --- | --- |
| `sgs` | Generate a random SGS (sex/gender/sexuality) string |
| `role` | Generate a random role string |
| `stats <mode>` | Generate random stats using the given mode |
| `life [age]` | Generate life-path events for the specified age, or a random age from 18–28 |
| `motivations` | Generate a random character personality and motivation set |

### Stat generation modes

| Mode | Description |
| --- | --- |
| `9d10` | Roll 9d10 and return the total CP for the user to distribute |
| `d10` | Roll d10 for every stat, with a minimum of 3 |

### Life-path generation

The `life` command generates events for each year from age 16 through the selected age.
The age must be an integer greater than 16.
When omitted, it defaults to a random age from 18–28 (`2d6 + 16`).

### Motivation generation

The `motivations` command generates a character personality, the person and concept they value most, their attitude toward other people, and their most-valued possession category.

---

## Examples

Generate a random SGS string:

```bash
$ cyberpunk_tools character sgs
F/NB/Pan
```

Generate a random role:

```bash
$ cyberpunk_tools character role
Netrunner
```

Generate life-path events for a random age:

```bash
$ cyberpunk_tools character life
Age: 24
===============================================
2006: Big Prob/big wins : lucky event : financial windfall : +400ed
2007: Frenemies : made friend : old childhood friend
```

Generate life-path events for a specific age:

```bash
$ cyberpunk_tools character life 30
```

Roll a CP pool to distribute (9d10):

```bash
$ cyberpunk_tools character stats 9d10
CP to distribute between stats: 47
```

Roll a full stat block (d10, min 3):

```bash
$ cyberpunk_tools character stats d10
Stats:
int :  7
ref :  5
tech: 10
cool:  4
attr:  8
luck:  6
mov :  3
body:  9
emp :  5
```

Generate a character motivation set:

```bash
$ cyberpunk_tools character motivations
Motivations:
Personality: Friendly and outgoing
Person you value most: Yourself
What you value most: Friendship
How you feel about most people: People are wonderful
Your most valued possession: A photograph
```

Check the version:

```bash
$ cyberpunk_tools --version
cyberpunk tools version: 0.0.9
```

---

## SGS Output Format

The `sgs` command prints a string in the format `sex/gender/sexuality`.

**Sex**
- `M` - Male
- `F` - Female
- `IF` - Intersex, Female appearance
- `IM` - Intersex, Male appearance
- `IA` - Intersex, Androgynous appearance

**Gender**
- `M` - Male
- `F` - Female
- `NB` - Non-binary
- `GF` - Gender fluid

**Sexuality**
- `Hete` - Heterosexual
- `Homo` - Homosexual
- `Bi` - Bisexual
- `A` - Asexual
- `Pan` - Pansexual


## Extending

The codebase is intentionally small and flat. To add a new tool:

1. Add a `<tool>()` function near the existing functions, including a docstring that describes its parameters, return value, and any side effects.
2. Wire it into a fitting option branch of `__main__` (`character`, ...) or create one.
3. Update `print_help()` and this README.


## Legal & Disclaimer

`cyberpunk_tools` is unofficial content provided under the **Homebrew Content Policy of R. Talsorian Games** and is **not approved or endorsed by RTG**.   
This content references materials that are the property of R. Talsorian Games and its licensees.

### Distribution

This content is provided **entirely free of charge** and is **not distributed via retail marketplaces** such as DriveThruRPG or itch.io.  
It is hosted openly on GitHub.

### Content Usage

This tool uses game mechanics, role names, and Lifepath tables for **automation and summarization only**. It does **not** reproduce full descriptive text, stat blocks, or rulesets from R. Talsorian Games products.

### Removal Requests

R. Talsorian Games reserves the right to request removal of this content from any platform for any reason. Removal requests may be made to:

> homebrewcyberpunktools@gmail.com

Upon receipt of a removal request, this content will be promptly removed from distribution.

---

## License

This project is released under the terms of the R. Talsorian Games Homebrew Content Policy. See the full policy text in [License](LICENSE) for details.