import os
import sys
import operator as _operator


outputs = list()


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def handle_op(param1, param2, param3, commands, op, mode1, mode2, mode3):
    operator_mapping = {
        '+': _operator.add,
        '*': _operator.mul,
    }
    if mode1 != 1:
        param1 = commands[param1]
    if mode2 != 1:
        param2 = commands[param2]
    result = operator_mapping[op](param1, param2)
    commands[param3] = result


def handle_input(param1, commands):
    commands[param1] = int(input('input: '))


def handle_output(param1, commands, mode):
    if mode != 1:
        param1 = commands[param1]
    outputs.append(param1)


def handle_jump_if_true(param1, param2, commands, mode1, mode2):
    if mode1 != 1:
        param1 = commands[param1]
    if mode2 != 1:
        param2 = commands[param2]
    if param1 != 0:
        result = param2
        return result


def handle_jump_if_false(param1, param2, commands, mode1, mode2):
    if mode1 != 1:
        param1 = commands[param1]
    if mode2 != 1:
        param2 = commands[param2]
    if param1 == 0:
        result = param2
        return result


def handle_less_than(param1, param2, param3, commands, mode1, mode2):
    if mode1 != 1:
        param1 = commands[param1]
    if mode2 != 1:
        param2 = commands[param2]
    if param1 < param2:
        commands[param3] = 1
    else:
        commands[param3] = 0


def handle_equals(param1, param2, param3, commands, mode1, mode2):
    if mode1 != 1:
        param1 = commands[param1]
    if mode2 != 1:
        param2 = commands[param2]
    if param1 == param2:
        commands[param3] = 1
    else:
        commands[param3] = 0


def handle_instruction(opcode, commands, index, mode1=0, mode2=0, mode3=1):
    if opcode == 1 or opcode == 2:
        param1 = commands[index + 1]
        param2 = commands[index + 2]
        param3 = commands[index + 3]
        if opcode == 1:
            handle_op(param1, param2, param3, commands,
                      '+', mode1, mode2, mode3)
        else:
            handle_op(param1, param2, param3, commands,
                      '*',  mode1, mode2, mode3)
        index = index + 4
    elif opcode == 3:
        param1 = commands[index + 1]
        handle_input(param1, commands)
        index = index + 2
    elif opcode == 4:
        param1 = commands[index + 1]
        handle_output(param1, commands, mode1)
        index = index + 2
    elif opcode == 5:
        param1 = commands[index + 1]
        param2 = commands[index + 2]
        result = handle_jump_if_true(param1, param2, commands, mode1, mode2)
        if result is not None:
            index = result
        else:
            index = index + 3
    elif opcode == 6:
        param1 = commands[index + 1]
        param2 = commands[index + 2]
        result = handle_jump_if_false(param1, param2, commands, mode1, mode2)
        if result is not None:
            index = result
        else:
            index = index + 3
    elif opcode == 7:
        param1 = commands[index + 1]
        param2 = commands[index + 2]
        param3 = commands[index + 3]
        handle_less_than(param1, param2, param3, commands, mode1, mode2)
        index = index + 4
    elif opcode == 8:
        param1 = commands[index + 1]
        param2 = commands[index + 2]
        param3 = commands[index + 3]
        handle_equals(param1, param2, param3, commands, mode1, mode2)
        index = index + 4
    elif opcode == 99:  # exit
        return len(commands)
    else:
        instruction = str(opcode).zfill(5)
        opcode = int(instruction[3:])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])
        index = handle_instruction(opcode, commands,
                                   index, mode1, mode2, mode3)
    return index


def main():
    file_path = f'{get_script_path()}\\original_input.txt'
    with open(file_path, 'r') as input_file:
        lines = input_file.read()

    lines = lines.split(',')
    commands = [int(number) for number in lines]
    index = 0
    while index < len(commands):
        opcode = commands[index]
        try:
            index = handle_instruction(
                opcode, commands, index, mode1=0, mode2=0, mode3=1)

        except Exception as ex:
            print(f'exception on command {opcode} at index {index}\n{ex}')
            break
    print('diagnostic code =', outputs[-1])


if __name__ == '__main__':
    main()
