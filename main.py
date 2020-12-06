# 01 report repair

def sum_of_two(sum, array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            if array[i] + array[j] == sum:
                return array[i], array[j]


def sum_of_three(sum, array):
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i == j or i == k or j == k:
                    continue
                if array[i] + array[j] + array[k] == sum:
                    return array[i], array[j], array[k]


def solve_01():
    file_name = '01_report_repair/input.txt'
    file = open(file_name, 'r')
    lines = file.readlines()
    # print(lines)

    # 01_report_repair
    numbers = []
    for l in lines:
        if l == '\n':
            continue
        numbers.append(int(l[:-1]))
    a, b = sum_of_two(2020, numbers)
    print(a * b)

    a, b, c = sum_of_three(2020, numbers)
    print(a * b * c)


# 02 password philosophy

def split_low_high_char_pw(line):
    low_split = line.split('-')
    low = int(low_split[0])

    high_split = low_split[1].split(' ')
    high = int(high_split[0])

    char_with_colon = high_split[1]
    pw = high_split[2]

    char = char_with_colon[:-1]

    return low, high, char, pw


def solve_02():
    file_name = '02_password_philosophy/input.txt'
    file = open(file_name, 'r')
    lines = file.readlines()
    
    low_high_valid = 0
    occurrence_valid = 0
    for l in lines:
        low, high, char, pw = split_low_high_char_pw(l[:-1])
        # print(pw)
        occurrence = 0
        for c in pw:
            if c == char:
                occurrence += 1
        if occurrence >= low and occurrence <= high:
            low_high_valid += 1

        if pw[low - 1] == char and pw[high - 1] == char:
            continue
        elif pw[low - 1] == char or pw[high - 1] == char:
            occurrence_valid += 1
        else:
            continue

    # raise NotImplementedError
    print(low_high_valid)
    print(occurrence_valid)


if __name__ == '__main__':
    # solve_01()
    solve_02()