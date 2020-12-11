# def get_num_occupied(spaces, r, c):

import copy

def is_occupied(spaces, r, c):
    if r < 0 or r >= len(spaces):
        return False
    if c < 0 or c >= len(spaces[r]):
        return False
    if spaces[r][c] == '#':
        return True
    return False

def get_adjacent(spaces, r, c):
    occupied = 0
    if is_occupied(spaces, r-1, c-1):
        occupied += 1
    
    if is_occupied(spaces, r-1, c):
        occupied += 1

    if is_occupied(spaces, r-1, c+1):
        occupied += 1

    if is_occupied(spaces, r, c-1):
        occupied += 1

    if is_occupied(spaces, r, c+1):
        occupied += 1

    if is_occupied(spaces, r+1, c-1):
        occupied += 1

    if is_occupied(spaces, r+1, c):
        occupied += 1

    if is_occupied(spaces, r+1, c+1):
        occupied += 1

    return occupied


# def direction_is_occupied(spaces, r, c, row_diff, col_diff):
#     target_row = r + row_diff
#     target_col = c + col_diff
#     if target_row < 0 or target_row >= len(spaces):
#         return False
#     if 

# def get_somet


# def get_visible_seats(spaces, r, c):
    



def one_round(spaes):
    new_spaces = copy.deepcopy(spaes)
    for r in range(len(spaes)):
        for c in range(len(spaes[r])):
            curr = spaes[r][c]
            num = get_adjacent(spaes, r, c)
            if curr == 'L' and num == 0:
                new_spaces[r][c] = '#'
            elif curr == '#' and num >= 4:
                new_spaces[r][c] = 'L'
            else:
                continue
    return new_spaces


def compare(past, new):
    for r in range(len(past)):
        for c in range(len(past[r])):
            if past[r][c] != new[r][c]:
                return False
    return True

def find_occupied(spaces):
    num = 0
    for r in range(len(spaces)):
        for c in range(len(spaces[r])):
            if spaces[r][c] == '#':
                num += 1
    return num

def is_valid(spaces, r, c):
    if r < 0 or r >= len(spaces):
        return False
    if c < 0 or c >= len(spaces[r]):
        return False
    return True

def is_direction_occupied(spaces, r, c, d):
    # print(d)
    tr = r + d[0]
    tc = c + d[1]
    if not is_valid(spaces, tr, tc):
        return False
    t = spaces[tr][tc]
    done = False
    while not done:
        if t == 'L':
            return False
        if t == '#':
            return True
        if t == '.':
            tr += d[0]
            tc += d[1]
            if not is_valid(spaces, tr, tc):
                return False
            t = spaces[tr][tc]

def get_visible(spaces, r, c):
    directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]]
    occupied = 0
    for d in directions:
        if is_direction_occupied(spaces, r, c, d):
            occupied += 1
    return occupied


def one_round_visible(spaces):
    new_spaces = copy.deepcopy(spaces)
    for r in range(len(spaces)):
        for c in range(len(spaces[r])):
            curr = spaces[r][c]
            num = get_visible(spaces, r, c)
            if curr == 'L' and num == 0:
                new_spaces[r][c] = '#'
            elif curr == '#' and num >= 5:
                new_spaces[r][c] = 'L'
            else:
                continue
    return new_spaces

def main():
    file = open('input.txt', 'r')
    # file = open('input_test.txt', 'r')
    # file = open('input_test2.txt', 'r')
    lines = file.readlines()
    # print(lines)

    spaces = [[c for c in r[:-1]] for r in lines]

    num_iters = 0
    done = False
    while not done:
        # new_spaces = one_round(spaces)
        new_spaces = one_round_visible(spaces)
        num_iters += 1
        if compare(spaces, new_spaces):
            done = True
            break
        spaces = new_spaces

    print(num_iters)
    print(find_occupied(spaces))



if __name__ == '__main__':
    main()
