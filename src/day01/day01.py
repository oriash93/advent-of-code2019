from math import floor


def calc_fuel(mass):
    return floor(mass/3) - 2


def calc_fuel2(mass):
    masses = list()
    tmp = calc_fuel(mass)
    while tmp > 0:
        masses.append(tmp)
        tmp = calc_fuel(tmp)
    return masses


def main():
    file_path = 'D:\\Repositories\\advent-of-code2019\\src\\day01\\original_input.txt'
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()
    modules = [int(line.strip()) for line in lines]

    fuel_sum_pt1 = sum([calc_fuel(module_mass) for module_mass in modules])
    print('pt1', fuel_sum_pt1)

    fuel_sum_pt2 = 0
    for module_mass in modules:
        mass_of_masses = calc_fuel2(module_mass)
        fuel_sum_pt2 += sum(mass_of_masses)
    print('pt2', fuel_sum_pt2)


if __name__ == '__main__':
    main()
