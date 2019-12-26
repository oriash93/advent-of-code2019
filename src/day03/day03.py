def traverse(commands, positions_dict):
    positions = list()
    x, y = 0, 0
    steps = 0
    for command in commands:
        direction = command[0]
        delta = int(command[1:])
        if direction == 'U':
            for i in range(1, delta + 1):
                steps += 1
                y += 1
                positions.append((x, y))
                positions_dict[(x, y)] = steps
        elif direction == 'D':
            for i in range(1, delta + 1):
                steps += 1
                y -= 1
                positions.append((x, y))
                positions_dict[(x, y)] = steps
        elif direction == 'L':
            for i in range(1, delta + 1):
                steps += 1
                x -= 1
                positions.append((x, y))
                positions_dict[(x, y)] = steps
        elif direction == 'R':
            for i in range(1, delta + 1):
                steps += 1
                x += 1
                positions.append((x, y))
                positions_dict[(x, y)] = steps
        else:
            raise Exception('invalid!')
            return
    return positions


def intersect(col1, col2):
    return set(col1).intersection(col2)


def distance_from_origin(x, y):
    return abs(x) + abs(y)


def main():
    file_path = 'D:\\Repositories\\advent-of-code2019\\src\\day03\\original_input.txt'
    with open(file_path, 'r') as input_file:
        line1, line2 = input_file.readlines()

    positions_dict1 = dict()
    positions_dict2 = dict()
    commands1 = [command.strip() for command in line1.split(',')]
    positions1 = traverse(commands1, positions_dict1)
    commands2 = [command.strip() for command in line2.split(',')]
    positions2 = traverse(commands2, positions_dict2)
    intersections = intersect(positions1, positions2)
    part1 = min([distance_from_origin(x, y) for x, y in intersections])
    print('part1 =', part1)
    part2 = min([positions_dict1[intersection] + positions_dict2[intersection]
                 for intersection in intersections])
    print('part2 =', part2)


if __name__ == '__main__':
    main()
