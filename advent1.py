def single(vals):
    prev = -1
    count = -1
    for i in vals:
        if i > prev:
            count+=1
        prev = i
    
    print "single increments: ", count


def sumofthree(vals):
    prev_sum = -1
    count = -1
    for i in range(0, len(vals) - 2):
        curr_sum = vals[i] + vals[i+1] + vals[i+2]
        if curr_sum > prev_sum:
            count+=1
        prev_sum = curr_sum
    print "sum of 3 increments: ", count


if __name__=='__main__':
    vals = []
    f = open("input.txt", 'r')
    for line in f.readlines():
        vals.append(int(line))
    single(vals)
    sumofthree(vals)

