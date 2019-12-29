def check_order(num_str):
    return sorted(num_str) == list(num_str)


def check_duplicate(num_str):
    return any([num_str[i] == num_str[i+1] for i in range(0, len(num_str) - 1)])


def check_another(num_str):
    nums = set(list(num_str))
    nums_dict = dict.fromkeys(nums, 0)
    for num in nums:
        nums_dict[num] = num_str.count(num)
    return any([x == 2 for x in nums_dict.values()])


def main():
    count = 0
    count_2 = 0
    start = 108457
    end = 562041
    for num in range(start, end + 1):
        num_str = str(num)

        if len(num_str) == 6 and \
                check_order(num_str) and \
                check_duplicate(num_str):
            count += 1
            if check_another(num_str):
                count_2 += 1

    print('part1 =', count)
    print('part2 =', count_2)


if __name__ == '__main__':
    main()
