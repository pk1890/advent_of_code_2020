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


required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
f = open("input.txt")

passports = f.read().split("\n\n")
print(functools.reduce(operator.add, map(lambda x: int(required_fields.issubset(parse_passport(x).keys())), passports), 0))
