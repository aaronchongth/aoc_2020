import copy

def get_instruction(line):
    insts = line[:-1].split(' = ')
    # print(insts)

    inst = insts[0]
    return inst, insts[1]
    
def get_mem_loc(inst):
    # print(inst)
    num_split = inst.split('[')
    num_back_split = num_split[1].split(']')
    # print(num_back_split)
    return num_back_split[0]

def get_bit_str(num):
    return "{0:b}".format(num)

def make_bit_str_32bits(bit_str):
    need = 36 - len(bit_str)
    return (need * '0')  + bit_str

def get_masked_val(mask, long_bit_str):
    assert(len(mask) == len(long_bit_str))
    new = long_bit_str
    for i in range(len(mask)):
        if mask[i] != 'X':
            new = new[:i] + mask[i] + new[i+1:]
    return new

def back_to_int(bit_str):
    return int(bit_str, 2)

def find_total(add_space):
    sum = 0
    for k in add_space:
        sum += add_space[k]
    return sum

def is_done(addresses):
    for a in addresses:
        for i in range(len(a)):
            if a[i] == 'X':
                return False
    return True

def is_address_clean(a):
    for i in range(len(a)):
        if a[i] == 'X':
            return False
    return True

def are_addresses_clean(addresses):
    for a in addresses:
        if not is_address_clean(a):
            return False
    return True

def get_perms(floating, considered_addresses):
    if floating in considered_addresses:
        return []

    if not is_address_clean(floating):
        new_perms = []
        for i in range(len(floating)):
            if floating[i] == 'X':
                first = floating[:i] + '0' + floating[i+1:]
                if first not in considered_addresses:
                    new_perms += get_perms(first, considered_addresses)
                    considered_addresses.append(first)

                second = floating[:i] + '1' + floating[i+1:]
                if second not in considered_addresses:
                    new_perms += get_perms(second, considered_addresses)
                    considered_addresses.append(second)

                # for f in get_perms(first):
                #     if f not in new_perms:
                #         new_perms += f
                # for s in get_perms(second):
                #     if s not in new_perms:
                #         new_perms += s

        return new_perms
    else:
        return [floating]

# def get_permutations(floating):
#     new_addresses = [floating]
#     while not are_addresses_clean(new_addresses):
#         new_new_addresses = []
#         for a in new_addresses:
#             for i in range(len(a)):
#                 if a[i] == 'X':
#                     first = a[:i] + '0' + a[i+1:]
#                     second = a[:i] + '1' + a[i+1:]
#                     new_new_addresses.append(first)
#                     new_new_addresses.append(second)
#                 else:
#                     new_new_addresses.append(a)
#     return new_addresses

def get_addresses(mask, add):
    # assert(len(mask) == len(add))
    add_with_float = add
    for i in range(len(mask)):
        if mask[i] != '0':
            add_with_float = add_with_float[:i] + mask[i] + add_with_float[i+1:]
    print('____', add_with_float)
    considered_addresses = []
    return get_perms(add_with_float, considered_addresses)

def get_masked_addresses(mask, add):
    # assert(len(mask) == len(add))
    add_with_float = add
    for i in range(len(mask)):
        if mask[i] != '0':
            add_with_float = add_with_float[:i] + mask[i] + add_with_float[i+1:]
    print('____', add_with_float)
    return add_with_float

# def find_total_perms(add_space):
#     sum = 0
#     for k in add_space:
#         masked_add = add_space[k]
#         num_x = 0
#         for i in range(len(masked_add)):
#             if masked_add[i] == 'X':
#                 num_x += 1
#         num_perms = 

def get_int_addresses(masked_add):
    adds = []
    curr_vals = [0]
    for i, c in enumerate(reversed(masked_add)):
        # print(c)
        new_curr_vals = []
        if c == 'X':
            for v in curr_vals:
                new_curr_vals.append(v)
                new_curr_vals.append(v + 2**i)
            curr_vals = new_curr_vals
        elif c == '1':
            for v in curr_vals:
                new_curr_vals.append(v + 2**i)
            curr_vals = new_curr_vals
        elif c == '0':
            continue
        else:
            assert False
    return curr_vals

def main():
    # print(get_bit_str(42))
    # print(back_to_int('00000000000001001'))

    file = open('input.txt', 'r')
    # file = open('input_test.txt', 'r')
    # file = open('input_test2.txt', 'r')
    lines = file.readlines()
    # print(lines)

    add_space = {}
    curr_mask = ''
    for l in lines:
        inst, inst2 = get_instruction(l)
        if inst == 'mask':
            curr_mask = inst2
            print('mask', curr_mask)
            continue
        
        address = get_mem_loc(inst)
        val = int(inst2)
        # bit_str = get_bit_str(val)
        bit_str = get_bit_str(int(address))
        long_bit_str = make_bit_str_32bits(bit_str)
        print('    ', long_bit_str)
        
        # mask_long_bit_str = get_masked_val(curr_mask, long_bit_str)
        # # print(mask_long_bit_str)
        # # saved = 
        # # print(back_to_int(mask_long_bit_str))
        # add_space[address] = back_to_int(mask_long_bit_str)

        # curr_perm = get_addresses(curr_mask, long_bit_str)
        masked_add = get_masked_addresses(curr_mask, long_bit_str)
        # add_space[masked_add] = val
        # for c in curr_perm:
        #     # print('----', c)

        #     int_address = back_to_int(c)
        #     add_space[int_address] = val
        # #     # print('set {} to {}'.format(val, int_address))

        # import pdb
        # pdb.set_trace()

        int_adds = get_int_addresses(masked_add)
        print(int_adds)
        for i in int_adds:
            add_space[i] = val
            
    # for k in add_space:
    #     print(k, add_space[k])
    print(find_total(add_space))
    # print(find_total_perms(add_space))

if __name__ == '__main__':
    main()
