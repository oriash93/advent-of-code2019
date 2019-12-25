def traverse(commands):
    positions = list()
    x, y = 0, 0
    for command in commands:
        direction = command[0]
        delta = int(command[1:])
        if direction == 'U':
            for i in range(1, delta + 1):
                y += 1
                positions.append((x, y))
        elif direction == 'D':
            for i in range(1, delta + 1):
                y -= 1
                positions.append((x, y))
        elif direction == 'L':
            for i in range(1, delta + 1):
                x -= 1
                positions.append((x, y))
        elif direction == 'R':
            for i in range(1, delta + 1):
                x += 1
                positions.append((x, y))
        else:
            raise Exception('invalid!')
            return
    return positions


def intersect(col1, col2):
    return [item for item in col1 if item in col2]


def distance_from_origin(x, y):
    return abs(x) + abs(y)


def main():

    file_path = 'D:\\Repositories\\sandbox-py\\advent2019\\day03\\input3.txt'
    with open(file_path, 'r') as input_file:
        line1, line2 = input_file.readlines()

    commands1 = [command.strip() for command in line1.split(',')]
    positions1 = traverse(commands1)
    commands2 = [command.strip() for command in line2.split(',')]
    positions2 = traverse(commands2)
    intersections = intersect(positions1, positions2)
    part1 = min([distance_from_origin(x, y) for x, y in intersections])
    print('part1 =', part1)


if __name__ == '__main__':
    main()
