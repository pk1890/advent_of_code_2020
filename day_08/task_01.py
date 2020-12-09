f = open('input.txt')
instructions = [(command, int(number.rstrip())) for (command, number) in [tuple(line.split(' ')) for line in f.readlines()]]

acc = 0
pc = 0
visited = set()

instruction_handlers = {
    'nop': lambda acc, pc, num: (acc, pc+1),
    'jmp': lambda acc, pc, num: (acc, pc+num),
    'acc': lambda acc, pc, num: (acc+num, pc+1)
}

while pc not in visited:
    visited.add(pc)
    command, num = instructions[pc]
    acc, pc = instruction_handlers[command](acc, pc, num)

print(acc)