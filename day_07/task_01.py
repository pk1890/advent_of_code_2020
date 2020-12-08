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

def dfs_is_gold(graph, visited_verts, v):
    if v in visited_verts:
        return False
    if v == 'shiny gold':
        return True
    visited_verts.add(v)
    neighbours = get_neighbours(graph, v)
    return any(list(map(lambda color: dfs_is_gold(graph, visited_verts, color), neighbours)))



f = open('input.txt')
rules = f.readlines()

graph = {}
for rule in rules:
    color, elements = parse_rule(rule)
    graph[color] = elements
print(len(list(
    filter(lambda x: x,
        map(lambda v: any([dfs_is_gold(graph, set(), neighbour) for neighbour in get_neighbours(graph, v)]), graph.keys())
    )
)))