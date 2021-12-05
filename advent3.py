
def calc_gamma(ones, zeros):
    max_pos = len(ones)
    bit = ""
    for i in range(0, max_pos):
        if ones[i] > zeros[i]:
            bit+="1"
        else:
            bit += "0"
    print bit
    return int(bit, 2)

def calc_epsilon(ones, zeros):
    max_pos = len(ones)
    bit = ""
    for i in range(0, max_pos):
        if ones[i] > zeros[i]:
            bit+="0"
        else:
            bit += "1"
    print bit
    return int(bit, 2)

def calc_bit_map(nums):
    bit_pos_map = {}
    for num in nums:
        pos = 0
        for b in num:
            if pos not in bit_pos_map:
                bit_pos_map[pos] = 0
            if b == '0':
                bit_pos_map[pos] -= 1
            if b == '1':
                bit_pos_map[pos] += 1
            pos += 1
    return bit_pos_map


def oxygen_generator():
    nums = []
    with open("input3.txt", 'r') as f:
        for line in f.readlines():
            nums.append(line.strip('\n'))
    
    pos = 0
    while (len(nums) > 1):
        bit_pos_map = calc_bit_map(nums)
        to_remove = []
        for n in nums:
            if bit_pos_map[pos] == 0 and n[pos] != '1':
                to_remove.append(n)
            
            if bit_pos_map[pos] > 0 and n[pos] == '0':
                to_remove.append(n)

            if bit_pos_map[pos] < 0 and n[pos] == '1':
                to_remove.append(n)

        for n in to_remove:
            nums.remove(n)
        pos+=1
    
    print "o2", int(nums[0], 2)
    return int(nums[0], 2)

def co2_scrubber():
    nums = []
    with open("input3.txt", 'r') as f:
        for line in f.readlines():
            nums.append(line.strip('\n'))
    
    pos = 0
    while (len(nums) > 1):
        bit_pos_map = calc_bit_map(nums)
        to_remove = []
        for n in nums:
            if bit_pos_map[pos] == 0 and n[pos] != '0':
                to_remove.append(n)
            
            if bit_pos_map[pos] > 0 and n[pos] == '1':
                to_remove.append(n)

            if bit_pos_map[pos] < 0 and n[pos] == '0':
                to_remove.append(n)

        for n in to_remove:
            nums.remove(n)
        pos+=1
    
    print "co2", int(nums[0], 2)
    return int(nums[0], 2)


if __name__=="__main__":
    ones = {}  
    zeros = {}
    with open("input3.txt", 'r') as f:
        for line in f.readlines():
            pos = 0
            for bit in line.strip('\n'):
                if pos not in ones:
                    ones[pos] = 0
                if pos not in zeros:
                    zeros[pos] = 0
                if bit == '0':
                    zeros[pos]+=1
                if bit == '1':
                    ones[pos]+=1
                pos+=1

    gamma = calc_gamma(ones, zeros)
    epsilon = calc_epsilon(ones, zeros)
    print "gamma ", gamma
    print "epsilon ", epsilon
    print "gamma*epsilon ", gamma * epsilon

    co2 = co2_scrubber()
    o2 = oxygen_generator()
    print "o2*co2 ", co2 * o2




