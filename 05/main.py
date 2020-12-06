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

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    rows = 128
    cols = 8

    seats = [[False for c in range(cols)] for r in range(rows)]
    all_ids = []
    highest_id = 0
    for l in lines:
        row = get_row(l)
        col = get_col(l)
        id = get_seat_id(row, col)

        seats[row][col] = True

        # info[id] = (row, col)
        all_ids.append(id)
        if id > highest_id:
            highest_id = id

    empty_seats = find_empty_seats(seats)
    solutions = []
    for s in empty_seats:
        if s[0] == 0 or s[0] == 127:
            continue
        id = get_seat_id(s[0], s[1])
        plus = id + 1
        minus = id - 1
        if plus in all_ids and minus in all_ids:
            solutions.append(id)

    print(solutions)
    

    # print(highest_id)
    # solutions = find_adjacents(info)
    # print(solutions)

if __name__ == '__main__':
    main()
