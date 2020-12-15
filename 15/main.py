import copy

# def get_num_age(mem, last_spoken):
#     if last_spoken not in mem:
#         return 0
#     else:
# def get_last_num_age(after_last, before_last, last_spoken, curr_turn):
#     if last_spoken in before_last:
#         that_turn = before_last[last_spoken]
#         new_turn = after_last[last_spoken]
#         return new_turn - that_turn
#     else:
#         return 0

# def get_what_to_say_next(mem, curr_turn, what_was_said_this_turn):
#     if last_spoken not in mem:
#         return 0
#     else:
#         that_turn = mem[what_was_said_this_turn]

def main():
    input = '0,3,6'
    # input = '12,20,0,6,1,17,7'

    mem = {}
    spoken = []
    nums = input.split(',')

    num = 2020
    curr_turn = 1
    starting_array_index = 0
    is_starting_done = False
    last_spoken = None
    while curr_turn != num and curr_turn < 8:
        if not is_starting_done:
            curr_num = int(nums[starting_array_index])
            spoken.append(curr_num)
            if curr_num in mem:
                mem[curr_num].append(curr_turn)
            else:
                mem[curr_num] = [curr_turn]

            # curr_turn += 1
            starting_array_index += 1
            if starting_array_index >= len(nums):
                is_starting_done = True
            # print(spoken)
            # print(mem)
        else:
            last_spoken = spoken[-1]
            # print(last_spoken)
            last_spoken_mem = mem[last_spoken]
            # print(last_spoken_mem)

            age = 0
            if len(last_spoken_mem) >= 2:
                age = last_spoken_mem[-1] - last_spoken_mem[-2]
            
            if age in mem:
                mem[age].append(curr_turn)
            else:
                mem[age] = [curr_turn]

            print(curr_turn, ' >>> ', last_spoken, last_spoken_mem, age, mem)
            spoken.append(age)
        curr_turn += 1
        # print(spoken)

    print(spoken[-1])

        #     if last_spoken in mem:
        #         last_spoken_turn = mem[last_spoken]
        #         mem[last_spoken] = curr_turn - 1
        #         last_spoken = curr_turn - 1 - last_spoken_turn
        #         curr_turn += 1
        #     else:
        #         mem[last_spoken] = curr_turn - 1
        #         last_spoken = 0
        #         curr_turn += 1

        # print(mem)
        # print(last_spoken)

        # if last_spoken not in mem:
        #     mem[last_spoken] = curr_turn - 1
        #     last_spoken = 0
        # else:
        #     that_turn = mem[last_spoken]
        #     age = curr_turn - that_turn
        #     mem[last_spoken] = curr_turn - 1
        #     last_spoken = age
        # curr_turn += 1
        # print(last_spoken)

    # print(last_spoken)

if __name__ == '__main__':
    main()
