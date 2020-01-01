import os
import sys
import operator as _operator


outputs = list()


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def handle_op(param1, param2, param3, data, op, mode1=0, mode2=0, mode3=1):
    operator_mapping = {
        '+': _operator.add,
        '*': _operator.mul,
    }
    if mode1 != 1:
        param1 = data[param1]
    if mode2 != 1:
        param2 = data[param2]
    if mode3 != 1:
        param3 = data[param3]
    result = operator_mapping[op](param1, param2)
    data[param3] = result


def handle_input(param1, data, mode=0):
    data[param1] = int(input('input: '))


def handle_output(param1, data, mode=0):
    if mode != 1:
        param1 = data[param1]
    outputs.append(param1)


def handle_complex(instruction, data, index):
    opcode = int(instruction[3:])
    mode1 = int(instruction[2])
    mode2 = int(instruction[1])
    mode3 = int(instruction[0])
    if opcode == 1 or opcode == 2:
        param1 = data[index + 1]
        param2 = data[index + 2]
        param3 = data[index + 3]
        if opcode == 1:
            handle_op(param1, param2, param3, data,
                      '+', mode1, mode2)
        else:
            handle_op(param1, param2, param3, data,
                      '*', mode1, mode2)
        index = index + 4
    elif opcode == 3:
        param1 = data[index + 1]
        handle_input(param1, data)
        index = index + 2
    elif opcode == 4:
        param1 = data[index + 1]
        handle_output(param1, data, mode1)
        index = index + 2
    elif command == 99:
        print('exit!')
    return index


def run(commands_list):
    index = 0
    while index < len(commands_list):
        opcode = commands_list[index]
        try:
            if opcode == 1 or opcode == 2:
                param1 = commands_list[index + 1]
                param2 = commands_list[index + 2]
                param3 = commands_list[index + 3]
                if opcode == 1:
                    handle_op(param1, param2, param3, commands_list, op='+')
                else:
                    handle_op(param1, param2, param3, commands_list, op='*')
                index = index + 4
            elif opcode == 3:
                param1 = commands_list[index + 1]
                handle_input(param1, commands_list)
                index = index + 2
            elif opcode == 4:
                param1 = commands_list[index + 1]
                handle_output(param1, commands_list)
                index = index + 2
            elif opcode == 99:
                print('exit')
                break
            else:
                instruction = str(opcode).zfill(5)
                index = handle_complex(instruction, commands_list, index)
        except Exception as ex:
            print(f'exception on command at index {index}: {opcode}\n{ex}')
            break


def main():
    file_path = f'{get_script_path()}\\original_input.txt'
    with open(file_path, 'r') as input_file:
        lines = input_file.read()

    lines = lines.split(',')
    commands_list = [int(number) for number in lines]
    run(commands_list)
    print('part1 =', outputs[-1])


if __name__ == '__main__':
    main()
