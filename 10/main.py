import copy

def find_perm(jolts, curr_sequence):
    max_jolt = max(jolts)
    adapter = max_jolt + 3

    perms = 0
    curr_max = curr_sequence[-1]

    within = 3
    for j in jolts:
        if j <= curr_max:
            continue
        if j == max_jolt:
            return 1
        if j - curr_max <= 3:
            perms += find_perm(jolts, curr_sequence.append(j))

def make_new_list(old_list):
    new_list = []
    for i in old_list:
        new_list.append(i)
    return new_list

# def 

def traverse_get_permutation(curr_num, next_map, current_value, adapter):
    nexts = next_map[curr_num]
    value = current_value * len(nexts)
    total = 0
    for n in nexts:
        if n == adapter:
            continue
        total += current_value * traverse_get_permutation(n, next_map, value, adapter)
    return total


    # value = 0
    # for i in next_map:
    #     this_val = vals[i]
    #     nexts = next_map[i]
    #     for n in nexts:
    #         value += this_val * traverse_get_val()

def simple_traverse(curr_num, next_map, adapter, found_nums):
    if curr_num == adapter:
        return 1
    if curr_num in found_nums:
        return found_nums[curr_num]

    nexts = next_map[curr_num]
    paths_from_curr = 0
    for n in nexts:
        paths_from_curr += simple_traverse(n, next_map, adapter, found_nums)

    found_nums[curr_num] = paths_from_curr
    return paths_from_curr

def main():
    file = open('input.txt', 'r')
    # file = open('input_test.txt', 'r')
    # file = open('input_test2.txt', 'r')
    lines = file.readlines()
    # print(lines)

    jolts = []
    for l in lines:
        jolts.append(int(l[:-1]))

    max_jolt = max(jolts)
    adapter = max_jolt + 3

    next_map = {}
    sorted_jolts = sorted(jolts)
    sorted_jolts = [0] + sorted_jolts + [adapter]
    for j in sorted_jolts:
        if j == adapter:
            continue
        next = []
        for k in sorted_jolts:
            if k <= j:
                continue
            if k - j <= 3:
                next.append(k)
        next_map[j] = next
    # print(next_map)

    print(simple_traverse(0, next_map, adapter, {}))

    # parents = {}
    # reverse_jolts = reversed(sorted_jolts)
    # for r in reverse_jolts:
    #     n_p = []
    #     for n in next_map:
    #         if r in next_map[n]:
    #             n_p.append(n)
    #     parents[r] = n_p
    # print(parents)



    # vals = {}
    # reverse_jolts = reversed(sorted_jolts)
    # for r in reverse_jolts:
    #     if r == adapter:
    #         continue
    #     vals[r] = len(next_map[r])
    # # print(vals)

    # print(traverse_get_permutation(0, next_map, 0, adapter))

    # total = 1
    # for v in vals:
    #     curr_val = vals[v]
    #     if curr_val > 1:
    #         total += curr_val
    # print(total)

    # last_numbers = [0]
    # sorted_jolts = sorted(jolts)
    # done = False
    # while not done:
    #     for l in last_numbers:
    #         if l == max_jolt:
    #             continue
    #         for s in sorted_jolts:
    #             if s <= l:
    #                 continue
    #             if s - l <= 3:
    #                 last_numbers.append(s)
    #     all_done = True
    #     for l in last_numbers:
    #         if l != max_jolt:
    #             all_done = False

    # print(len(last_numbers))


    # sequence = [0]
    # permutations = []
    # permutations.append(sequence)
    # not_done = 1

    # while not_done > 0:
    #     new_permutations = []
    #     new_not_done = 0

    #     for p in permutations:
    #         p_largest = p[-1]
    #         for j in sorted_jolts:
    #             if j <= p_largest:
    #                 continue
    #             if j - p_largest <= 3:
    #                 new_sequence = copy.deepcopy(p)
    #                 new_sequence.append(j)
    #                 new_permutations.append(new_sequence)

    #                 if j != max_jolt:
    #                     new_not_done += 1
        
    #     permutations = new_permutations
    #     not_done = new_not_done

    # print(len(permutations))


    # diff_1 = 0
    # diff_3 = 0
    # while len(sequence) != len(jolts) + 2:
    #     # print(l[:-1])

    #     curr_smallest = max(jolts)
    #     for j in jolts:
    #         if j in sequence:
    #             continue
    #         if j < curr_smallest:
    #             curr_smallest = j

    #     last_s = sequence[-1]

    #     if curr_smallest - last_s == 1:
    #         diff_1 += 1
    #     elif curr_smallest - last_s == 3:
    #         diff_3 += 1
    #     else:
    #         print('what', curr_smallest, last_s)

    #     if curr_smallest in sequence:
    #         break
    #     sequence.append(curr_smallest)


    # last = sequence[-1]
    # if adapter - last == 1:
    #     diff_1 += 1
    # elif adapter - last == 3:
    #     diff_3 += 1
    # else:
    #     print('what', adapter, last)
    # sequence.append(adapter)
    # print(sequence)

    # print(diff_1 * diff_3)

    # print(find_perm(jolts, sequence))

if __name__ == '__main__':
    main()
