def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    # print(lines)
    # required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
    required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

    valid = 0
    person_fields = []
    passports = []
    curr_passport = {}
    for l in lines:
        if l == '\n':
            # evaluate the current person
            # is_valid = True
            # print(person_fields)
            # for r in required:
            #     if r not in person_fields:
            #         print(r)
            #         is_valid = False
            # if is_valid:
            #     valid += 1
            # person_fields = []
            passports.append(curr_passport)
            curr_passport = {}
            continue
        else:
            l = l[:-1]
            # print(l)
            stuff = l.split(' ')
            # print(stuff)
            for f in stuff:
                info = f.split(':')
                # person_fields.append(info[0])
                curr_passport[info[0]] = info[1]
                # if info[0] not in required:
                #     print(info[0])

    invalid = 0
    for p in passports:
        is_valid = True
        for r in required:
            if r not in p:
                is_valid = False
                invalid += 1
                break
        if is_valid:
            byr = int(p['byr'])
            iyr = int(p['iyr'])
            eyr = int(p['eyr'])
            hgt_end = p['hgt'][-2:]
            # try:
            #     hgt = int(p['hgt'][:-2])
            # except:
            #     invalid += 1
            #     continue
            # print(p['hgt'][:-2])
            if len(p['hgt'][:-2]) < 2:
                invalid += 1
                print('hgt short')
                continue
            hgt = int(p['hgt'][:-2])
            # print(hgt)
            hcl = p['hcl']
            ecl = p['ecl']
            pid = p['pid']

            if byr < 1920 or byr > 2002 or \
              iyr < 2010 or iyr > 2020 or \
              eyr < 2020 or eyr > 2030:
              invalid += 1
              print('years wrong')
              continue

            if hgt_end == 'cm':
                if hgt < 150 or hgt > 193:
                    invalid += 1
                    print('hgt cm invalid')
                    continue
            elif hgt_end == 'in':
                if hgt < 59 or hgt > 76:
                    invalid += 1
                    print('hgt in invalid')
                    continue
            # else:
            #     invalid += 1
            #     continue
            
            valid_chars = '0123456789abcdef'
            if hcl[0] != '#':
                invalid += 1
                print('not pount')
                continue
            else:
                is_invalid = False
                for c in hcl[1:]:
                    if c not in valid_chars:
                        print('not in valid_chars')
                        print(c)
                        is_invalid = True
                if is_invalid:
                    invalid += 1
                    continue

            valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if ecl not in valid_ecl:
                invalid += 1
                print('ecl not valid')
                print(hcl)
                continue
            
            valid_id = '0123456789'
            if len(pid) != 9:
                invalid += 1
                print('pid not 9')
                continue
            is_invalid = False
            for p in pid:
                if p not in valid_id:
                    is_invalid = True
                    print('not in pid')
                    print(p)
            if is_invalid:
                invalid += 1
                continue

            # if int(p['byr']) >= 1920 and int(p['byr']) <= 2002:
            #     if int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020:
            #         if int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030:
                        
            # valid += 1

    # map = [l[:-1] for l in lines]
    # print(map)
    print(invalid)
    print(len(passports))
    print(len(passports) - invalid)
    # print(valid)

if __name__ == '__main__':
    main()
