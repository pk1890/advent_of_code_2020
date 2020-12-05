import re
import functools
import operator

def parse_passport(passport):
    result = {}
    tokens = re.split('[ \n]', passport)
    for token in tokens:
        [key, val] = token.split(':')
        result[key] = val
    return result

def between(val, min, max):
    return val >= min and val <= max

required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


rules = {
    "byr": lambda x: len(x) == 4 and between(int(x), 1920, 2002),
    "iyr": lambda x: len(x) == 4 and between(int(x), 2010, 2020),
    "eyr": lambda x: len(x) == 4 and between(int(x), 2020, 2030),
    "hgt": lambda x: (re.fullmatch(r'\d+in', x) and between(int(x[:-2]), 59, 76)) or (re.match("\d+cm", x) and between(int(x[:-2]), 150, 193)),
    "hcl": lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: re.fullmatch(r'\d{9}', x)
}

def validate_passport(passport):
    return int(required_fields.issubset(passport.keys()) and all(map(lambda key: rules[key](passport[key]), rules.keys())))


f = open("input.txt")

passports = f.read().split("\n\n")
print(functools.reduce(operator.add, map(validate_passport, (map(parse_passport, passports))), 0))