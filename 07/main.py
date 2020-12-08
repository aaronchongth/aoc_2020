def get_row(input):
    encoding = input[:7]
    left = 0
    right = 127
    for c in encoding:
        length = right - left + 1
        new_length = length / 2
        if c == 'F':
            right -= new_length
        elif c == 'B':
            left += new_length
    return int(left)

def get_col(input):
    encoding = input[-4:]
    left = 0
    right = 7
    for c in encoding:
        length = right - left + 1
        new_length = length / 2
        if c == 'L':
            right -= new_length
        elif c == 'R':
            left += new_length
    return int(left)

def get_seat_id(row, col):
    return (row * 8) + col

def find_adjacents(info):
    solutions = []
    for id in info:
        plus = id + 1
        minus = id - 1
        if plus in info and minus in info:
            solutions.append(info[id])
    return solutions

def find_empty_seats(seats):
    empty_seats = []
    for row_num in range(len(seats)):
        for col_num in range(len(seats[row_num])):
            if not seats[row_num][col_num]:
                empty_seats.append((row_num, col_num))
    return empty_seats

# def main():
#     file = open('input.txt', 'r')
#     lines = file.readlines()

#     rows = 128
#     cols = 8

#     seats = [[False for c in range(cols)] for r in range(rows)]
#     all_ids = []
#     highest_id = 0
#     for l in lines:
#         row = get_row(l)
#         col = get_col(l)
#         id = get_seat_id(row, col)

#         seats[row][col] = True

#         # info[id] = (row, col)
#         all_ids.append(id)
#         if id > highest_id:
#             highest_id = id

#     empty_seats = find_empty_seats(seats)
#     solutions = []
#     for s in empty_seats:
#         if s[0] == 0 or s[0] == 127:
#             continue
#         id = get_seat_id(s[0], s[1])
#         plus = id + 1
#         minus = id - 1
#         if plus in all_ids and minus in all_ids:
#             solutions.append(id)

#     print(solutions)
    
class Bags:
    def __init__(self, bags, bag_nums):
        self.bag_info = bags
        self.bag_nums = bag_nums

    def traverse(self, first_bag_name, target):
        first_bag_contains = self.bag_info[first_bag_name]
        # print(self.bag_info)
        # print(first_bag_contains)
        if target in first_bag_contains:
            return True
        else:
            for b in first_bag_contains:
                # print('checking ' + target + ' in ' + b)
                # print(bag_map[b])
                # if b == 'no other':
                #     continue
                if self.traverse(b, target):
                    return True
            return False
    
    def traverse_and_count(self, target):
        print('traversing ' + target)
        nums = self.bag_nums[target]
        colors = self.bag_info[target]
        print('it has ')
        print('    ', colors)
        if len(nums) == 0 and len(colors) == 0:
            return 0
        elif len(nums) != len(colors):
            print('something is wrong with colors and numbers')
            print(nums)
            print(colors)
            return 0

        tmp_bag = []
        for i in range(len(nums)):
            n = int(nums[i])
            c = colors[i]
            for k in range(n):
                tmp_bag.append(c)

        count = len(tmp_bag)
        for c in tmp_bag:
            count += self.traverse_and_count(c)
        return count

        # for n in nums:
        #     count += int(n)
        # for c in colors:
        #     count += self.traverse_and_count(c)
        #     return count

def main():
    file = open('input.txt', 'r')
    # file = open('input_test.txt', 'r')
    # file = open('input_test2.txt', 'r')
    lines = file.readlines()

    bag_info = {}
    bag_num_info = {}

    for l in lines:
        l = l[:-1]
        first_bag_split = l.split(' contain ')
        first_bag = first_bag_split[0]
        first_color_split = first_bag.split(' bag')
        first_color = first_color_split[0]
        # print(first_color)

        num_contains = []
        contains = []
        all_bag_splits = first_bag_split[1].split(', ')
        for bag in all_bag_splits:
            num_color_split = bag.split('bag')
            num_color = num_color_split[0]
            if num_color == 'no other ':
                continue
            # else:
            #     print(num_color)

            num_split = num_color.split(' ')
            num = num_split[0]
            color = num_split[1] + ' ' + num_split[2]
            # print(num, color)

            num_contains.append(num)
            contains.append(color)

        bag_info[first_color] = contains
        bag_num_info[first_color] = num_contains

    bags = Bags(bag_info, bag_num_info)
    # print(bag_info)
    target_color = 'shiny gold'
    at_least_one = 0
    # checked_bags = {}
    for c in bags.bag_info:
        # if c == 'no other':
        #     continue
        # curr_bag_contains = bag_info[c]
        # done_traversing = False
        # curr_search = c
        # while not done_traversing:

        if bags.traverse(c, target_color):
            at_least_one += 1

    # print(at_least_one)
    print(bags.traverse_and_count(target_color))


if __name__ == '__main__':
    main()
