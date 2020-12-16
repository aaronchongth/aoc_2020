import copy
import itertools

def check_field_range(field_range, num):
    if num < field_range[0] and num > field_range[1]:
        return False
    return True

def check_field_ranges(field_ranges, num):
    for r in field_ranges:
        if not check_field_range(r, num):
            return False
    return True

def check_possible_fields(possible_fields):
    for f in possible_fields:
        if len(f) != 1:
            return False
    return True

def main():
    # print(get_bit_str(42))
    # print(back_to_int('00000000000001001'))

    file = open('input.txt', 'r')
    # file = open('input_test.txt', 'r')
    # file = open('input_test2.txt', 'r')
    lines = file.readlines()
    # print(lines)

    valid_numbers = []
    valid_fields = []
    field_names = []
    are_fields_done = False
    invalid_numbers = []
    valid_tickets = []
    for l in lines:
        if l == '\n':
            are_fields_done = True
            continue
        # print(l)
        if not are_fields_done:            
            field_split = l[:-1].split(': ')
            field_names.append(field_split[0])
            # print(l)
            # print(field_split)
            ranges_split = field_split[1].split(' or ')
            curr_ranges = []
            for r in ranges_split:
                s = r.split('-')
                low = int(s[0])
                high = int(s[1])
                curr_ranges.append([low, high])
                for i in range(low, high + 1):
                    if i not in valid_numbers:
                        # curr_range.append(i)
                        valid_numbers.append(i)
            valid_fields.append(curr_ranges)

        else:
            if l[-2] == ':':
                # print(l)
                continue
                
            nums_split = l[:-1].split(',')
            curr_ticket = []
            for n in nums_split:
                num = int(n)
                if num not in valid_numbers:
                    invalid_numbers.append(num)
                    curr_ticket = []
                    break
                else:
                    curr_ticket.append(num)
            if len(curr_ticket) != 0:
                valid_tickets.append(curr_ticket)


    # for tix in valid_tickets:
    # print(valid_tickets)
    # print(valid_fields)
    # print(sum(invalid_numbers))
    # print(field_names)

    # field_indices = [x for x in range(len(valid_fields))]
    # # print(field_indices)
    # perms = list(itertools.permutations(field_indices))

    # perm_that_works = None
    # indices_that_did_not_work = [[] for x in range(len(perms[0]))]

    for p_i in range(len(perms)):
        curr_perm = perms[p_i]
        print('onto permutation: ', p_i, curr_perm)
        found_perm = False
        for i in range(len(curr_perm)):
            if curr_perm[i] in indices_that_did_not_work[i]:
                continue

        for i in range(len(curr_perm)):
            curr_index = curr_perm[i]
            ranges_to_check = valid_fields[curr_index]

            perm_valid = True
            for tix in valid_tickets:
                if not check_field_ranges(ranges_to_check, tix[i]):
                    perm_valid = False
                    break
            if not perm_valid:
                indices_that_did_not_work[i].append(curr_index)
                break
            else:
                perm_that_works = curr_perm
                found_perm = True
                break

        if found_perm:
            print(perm_that_works)
            break

    # Permutation stuff doesn't seem to work
    # possible_fields = [[x for x in range(len(valid_fields))] for i in range(len(valid_fields))]
    # # print(possible_fields)

    # for tix in valid_tickets:
    #     for i in range(len(tix)):
    #         print(possible_fields)
    #         num = tix[i]
    #         print('num: ', num)
    #         field_indices = possible_fields[i]
    #         print('field indices: ', field_indices)
    #         field_indices_to_ignore = []
    #         for f in field_indices:
    #             if f in field_indices_to_ignore:
    #                 continue
    #             ftc = valid_fields[f]
    #             if num not in ftc:
    #                 field_indices_to_ignore.append(f)
    #                 # field_indices.remove(f)
    #                 print(num, ftc)
    #                 print('removed: ', f)
    #                 # break
    #         for igf in field_indices_to_ignore:
    #             possible_fields[i].remove(igf)

    #     if check_possible_fields(possible_fields):
    #         print(possible_fields)
    #         break





if __name__ == '__main__':
    main()
