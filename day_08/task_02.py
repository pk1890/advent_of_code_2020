def interpret(instructions):
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
        if pc == len(instructions):
            return (True, acc)
        if pc > len(instructions):
            return (False, acc)
    return (False, acc)

f = open('input.txt')
instructions = [(command, int(number.rstrip())) for (command, number) in [tuple(line.split(' ')) for line in f.readlines()]]


for i in range(len(instructions)):
    command, num = instructions[i]
    if command == 'jmp':
        instructions[i] = ('nop', num)
    if command == 'nop':
        instructions[i] = ('jmp', num)
        
    flag, acc = interpret(instructions)
    if flag:
        print("Final acc: ", acc, "switch at command", i)
    
    instructions[i] = (command, num)
    