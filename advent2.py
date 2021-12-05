def total(vals):
    h = 0
    v = 0
    for s in vals:
        if (s[0] == "forward"):
            h += int(s[1])
        if (s[0] == "up"):
            v -= int(s[1])
        if (s[0] == "down"):
            v += int(s[1])
    print "horizontal ", h, " vertical ", v, " product ", v*h

def total_with_aim(input):
    h = 0
    v = 0
    aim = 0
    for s in input:
        if (s[0] == "forward"):
            h += int(s[1])
            v += aim * int(s[1])
        if (s[0] == "up"):
            aim -= int(s[1])
        if (s[0] == "down"):
            aim += int(s[1])

    print "horizontal ", h, " vertical ", v, " product ", v*h



if __name__ == "__main__":
    input = []

    with open('input2.txt', 'r') as f:
        for line in f.readlines():
            vals = line.split(" ")
            input.append((vals[0], vals[1].strip("\n")))

    total(input)
    total_with_aim(input)

