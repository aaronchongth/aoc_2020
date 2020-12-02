# import 

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    # for l in lines:
    #     print(l)
    
    valid = 0

    for l in lines:
        x = l.split('-')
        low = int(x[0])

        y = x[1].split(' ')
        high = int(y[0])
        char_with_colon = y[1]
        pw = y[2]

        char = char_with_colon[:-1]
        # print(char)

        # num = 0
        # for c in pw:
        #     if c == char:
        #         num += 1
        
        # if num >= low and num <= high:
        #     valid += 1

        if pw[low - 1] == char and pw[high - 1] == char:
            continue
        elif pw[low - 1] == char or pw[high - 1] == char:
            valid += 1
        else:
            continue
      

        # low_true = False
        # if low >= 1 and low <= len(pw):
        #     if pw[low - 1] == char:
        #         low_true = True

        # if high >= 1 and high <= len(pw):
        #     if pw[high - 1] == char:
        #         if low_true:
        #             continue
        #         else:
        #             valid += 1

    print(valid)

if __name__ == '__main__':
    main()
