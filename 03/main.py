def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    map = [l[:-1] for l in lines]
    # print(map)

    curr_row = 0
    curr_col = 0
    trees = 0
    done = False

#79
#216
#91
#96
#45


    while not done:
        if map[curr_row][curr_col] == '#':
            trees += 1
            print(trees)
        
        curr_row += 2
        if (curr_row > len(map)):
            done = True
            # print(trees)
            return

        curr_col += 1
        # print(len(map))
        # print(len(map[curr_row]))
        if (curr_col >= len(map[curr_row])):
            curr_col -= len(map[curr_row])
            # print(curr_col)



    # print(trees)


if __name__ == '__main__':
    main()
