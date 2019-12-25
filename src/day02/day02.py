from operator import add, mul


def process_action(param1, param2, op):
    return op(param1, param2)


def run(total_list, commands_list, goal):
    for command_list in commands_list:
        opcode = command_list[0]
        if opcode == 99:
            break
        else:
            num1 = command_list[1]
            num2 = command_list[2]
            dest = command_list[3]
            if opcode == 1:
                op = add
            elif opcode == 2:
                op = mul
            result = process_action(total_list[num1], total_list[num2], op)
            total_list[dest] = result
    return total_list[0] == goal


def run_wrapper(total_list, commands_list, goal):
    for noun in range(100):
        for verb in range(100):
            total_list[1] = noun
            total_list[2] = verb
            if run(total_list, commands_list, goal):
                print('noun is', noun, 'verb is', verb,
                      '\nanswer is', noun * 100 + verb)


def main():
    file_path = 'D:\\Repositories\\sandbox-py\\advent2019\\day02\\input.txt'
    with open(file_path, 'r') as input_file:
        lines = input_file.read()

    total_list = [int(number) for number in lines.split(',')]
    commands_list = [total_list[i:i + 4]
                     for i in range(0, len(total_list) - 3, 4)]

    run_wrapper(total_list, commands_list, goal=19690720)


if __name__ == '__main__':
    main()
