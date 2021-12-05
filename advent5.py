
def find_straight_hotspots(co_ords):
    c_map = {}
    hot_list = []

    for line in co_ords:
        if line[0][0] != line[1][0]  and line[0][1] != line[1][1]:
            continue
        x1 = int(line[0][0])
        x2 = int(line[1][0])
        y1 = int(line[0][1])
        y2 = int(line[1][1])
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, i) not in c_map:
                    c_map[x1, i] = 0
                c_map[x1, i] += 1
                if (c_map[x1, i] == 2):
                    hot_list.append((x1, i))
            continue
        
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                if (i, y1) not in c_map:
                    c_map[i, y1] = 0
                c_map[i, y1] += 1
                if (c_map[i, y1] == 2):
                    hot_list.append((i, y1))
    
    print "hotspot list size: ", len(hot_list)
    return len(hot_list)


def find_all_hotspots(co_ords):
    c_map = {}
    hot_list = []

    for line in co_ords:       
        x1 = int(line[0][0])
        x2 = int(line[1][0])
        y1 = int(line[0][1])
        y2 = int(line[1][1])      
     
        diagonal = False
        slope = 0
        c = 0

        if (x1!=x2 and y1!=y2):
            diagonal = True
            slope = (y2-y1)/(x2-x1)
            # y = mx +c
            c = y1 - slope*x1

        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                if (not diagonal or j == slope*i + c ):
                    if (i, j) not in c_map:
                        c_map[i, j] = 0
                    c_map[i, j] += 1
                    if (c_map[i, j] == 2):
                        hot_list.append((i, j))
    
    print "hotspot list size: ", len(hot_list)
    return len(hot_list)


if __name__ == "__main__":
    with open("input5.txt", 'r') as f:
        input = f.read()
        #[((x1, y1), (x2, y2)),...]
        co_ords = []
        lines = input.split("\n")
        for line in lines:
            co_ords_vec = line.strip("\t").split('->')
            first = co_ords_vec[0]
            c1 = (first.split(',')[0].strip(' '), first.split(',')[1].strip(' '))
            second = co_ords_vec[1]
            c2 = (second.split(',')[0].strip(' '), second.split(',')[1].strip(' '))
            co_ords.append((c1, c2))
    
    find_straight_hotspots(co_ords)
    find_all_hotspots(co_ords)
