def check_nums_before(lines, target_index, preamble_length):
    for i in range(preamble_length):
        for j in range(preamble_length):
            if i == j:
                continue
            first_num = int(lines[target_index - preamble_length + i][:-1])
            second_num = int(lines[target_index - preamble_length + j][:-1])
            if first_num + second_num == int(lines[target_index][:-1]):
                # print(i, first_num, j, second_num)
                return True
    return False

def find_contiguous(lines, elem_num, target_sum):
    for i in range(len(lines)):
        curr_sum = 0
        for j in range(elem_num):
            curr_sum += int(lines[i + j][:-1])
            if curr_sum > target_sum:
                break
        if curr_sum == target_sum:
            return i
        else:
            return -1

def find_sum_of_smallest_and_largest(lines, starting, num_elems):
    nums = []
    for i in range(num_elems):
        nums.append(int(lines[starting + i][:-1]))
    return sum(min(nums), max(nums))

def find_solution(lines, target_sum):
    nums = []
    for l in lines:
        nums.append(int(l[:-1]))

    for i in range(len(nums)):
        curr_smallest = 1e20
        curr_biggest = -1
        elems_left = len(nums) - i
        curr_sum = 0
        for j in range(elems_left):
            if j < 2:
                continue
            curr_num = nums[i + j]
            curr_sum += curr_num
            if curr_num < curr_smallest:
                curr_smallest = curr_num
            if curr_num > curr_biggest:
                curr_biggest = curr_num
            
            if curr_sum == target_sum:
                print('found sum ', i, j)
                print('vul ', curr_smallest + curr_biggest)
                return


def main():
    file = open('input.txt', 'r')
    # file = open('input_test.txt', 'r')
    # file = open('input_test2.txt', 'r')
    lines = file.readlines()
    # print(lines)

    # preamble_len = 5
    preamble_len = 25
    issue = -1
    for i in range(len(lines)):
        if i < preamble_len:
            continue
        if not check_nums_before(lines, i, preamble_len):
            issue = int(lines[i][:-1])
            print('found issue ', i, issue)
            break
        # print(num)

    # for j in range(len(lines)):
    #     if j < 2:
    #         continue
    #     starting_index = find_contiguous(lines, j, issue)
    #     if starting_index != -1:
    #         print('found the contig stuff, starting from ', starting_index, j)
    #         print('vul ', find_sum_of_smallest_and_largest(lines, starting_index, j))
    #         break
    find_solution(lines, issue)

if __name__ == '__main__':
    main()
