import copy

def run(lines):
    accum = 0
    visited = []
    curr_line = 0
    found_cycle = False
    while curr_line != len(lines):
        print(curr_line)
        if curr_line in visited:
            # print('found it')
            found_cycle = True
            break

        visited.append(curr_line)

        l = lines[curr_line][:-1]
        splits = l.split(' ')
        if splits[0] == 'nop':
            curr_line += 1
        elif splits[0] == 'acc':
            direction = splits[1][0]
            num = int(splits[1][1:])
            # print('adding the num', num)
            if direction == '+':
                accum += num
            elif direction == '-':
                accum -= num
            else:
                print('wtf at acc')
            curr_line += 1
        elif splits[0] == 'jmp':
            direction = splits[1][0]
            num = int(splits[1][1:])
            if direction == '+':
                curr_line += num
            elif direction == '-':
                curr_line -= num
            else:
                print('wtf at jmp')
    if found_cycle:
        print('ignore this')
    return accum


def modify_run(lines, modify_line):
    accum = 0
    visited = []
    curr_line = 0
    done = True
    # print('starting')
    while curr_line != len(lines):
        # print(curr_line)
        if curr_line in visited:
            done = False
            break

        visited.append(curr_line)

        l = lines[curr_line][:-1]
        splits = l.split(' ')
        if splits[0] == 'nop' and curr_line == modify_line:
            print('swapping out ', curr_line)
            direction = splits[1][0]
            num = int(splits[1][1:])
            if direction == '+':
                curr_line += num
            elif direction == '-':
                curr_line -= num
            else:
                print('wtf at jmp')
        elif splits[0] == 'jmp' and curr_line == modify_line:
            print('swapping out ', curr_line)
            curr_line += 1
        elif splits[0] == 'nop':
            curr_line += 1
        elif splits[0] == 'acc':
            direction = splits[1][0]
            num = int(splits[1][1:])
            # print('adding the num', num)
            if direction == '+':
                accum += num
            elif direction == '-':
                accum -= num
            else:
                print('wtf at acc')
            curr_line += 1
        elif splits[0] == 'jmp':
            direction = splits[1][0]
            num = int(splits[1][1:])
            if direction == '+':
                curr_line += num
            elif direction == '-':
                curr_line -= num
            else:
                print('wtf at jmp')

    if not done:
        return -1
    return accum


def main():
    file = open('input.txt', 'r')
    # file = open('input_test.txt', 'r')
    # file = open('input_test2.txt', 'r')
    lines = file.readlines()
    # print(lines)

    # fix it
    # start from the end
    # fixed = False
    # curr_line = len(lines) - 1
    # while not fixed:
    #     l = lines[curr_line][:-1]
    #     splits = l.split(' '):
    #     if splits[0] == 'nop':
    #         curr_line -= 1
    #     elif splits[0] == 'acc':
    #         curr_line
    for i in range(len(lines)):
        l = lines[i][:-1]
        splits = l.split(' ')
        if splits[0] == 'nop' or splits[0] == 'jmp':
            # result = modify_check_run(lines, i)
            # print(result)
            result = modify_run(lines, i)
            # print(result)
            if result == -1:
                continue
            else:
                print(result)
                break
    # print(run(lines))

    

    # accum = 0
    # visited = []
    # found = False
    # curr_line = 0
    # while not found:
    #     print(curr_line)
    #     if curr_line in visited:
    #         found = True
    #         print('found it')
    #         break

    #     visited.append(curr_line)

    #     l = lines[curr_line][:-1]
    #     splits = l.split(' ')
    #     if splits[0] == 'nop':
    #         curr_line += 1
    #     elif splits[0] == 'acc':
    #         direction = splits[1][0]
    #         num = int(splits[1][1:])
    #         print('adding the num', num)
    #         if direction == '+':
    #             accum += num
    #         elif direction == '-':
    #             accum -= num
    #         else:
    #             print('wtf at acc')
    #         curr_line += 1
    #     elif splits[0] == 'jmp':
    #         direction = splits[1][0]
    #         num = int(splits[1][1:])
    #         if direction == '+':
    #             curr_line += num
    #         elif direction == '-':
    #             curr_line -= num
    #         else:
    #             print('wtf at jmp')
            

    # print(accum)


if __name__ == '__main__':
    main()
