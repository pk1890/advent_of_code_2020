import re

def parse_rule(rule):
    elem_regex = re.compile("(\d+) (.*) bags?.*")
    rule = rule[:-1]
    color, inside = tuple(rule.split(" bags contain"))
    result = []
    for element in inside.split(","):
        match = elem_regex.search(element)
        if match:
            result.append((match.group(2), match.group(1)))
    return color, result

def get_neighbours(graph, v):
    return [color for color, _ in graph[v]]

def dfs_counting(graph, v):
    return 1+sum(list(map(lambda vert: int(vert[1]) * dfs_counting(graph, vert[0]), graph[v])))


f = open('input.txt')
rules = f.readlines()

graph = {}
for rule in rules:
    color, elements = parse_rule(rule)
    graph[color] = elements

print(dfs_counting(graph, 'shiny gold')-1) #we are not counting the shiny gold one, so we substract 1