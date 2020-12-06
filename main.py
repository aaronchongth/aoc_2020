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

def solve_02():
    raise NotImplementedError


if __name__ == '__main__':
    solve_01()
    solve_02()