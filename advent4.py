class Grid(object):
    def __init__(self, row, col):
        self.num_grid = {}
        self.cleared = {} 
        for i in range(row):
            self.cleared[('row', i)] = 0
        for i in range(col):
            self.cleared[('col', i)] = 0
        
def findWinner(grids, nums):
    for n in nums:
        grid_no = 0
        for g in grids:
            if n in g.num_grid:
                row_num, col_num = g.num_grid[n]
                g.cleared[("row", row_num)] += 1
                g.cleared[("col", col_num)] += 1
                del g.num_grid[n]


                if g.cleared["row", row_num] == 5 or g.cleared["col", col_num] == 5:
                    print "winner grid: ", grid_no

                    sum = 0
                    for key in g.num_grid:
                        sum += int(key)
                    print "winning number ", n
                    print "sum ", sum
                    print "answer ", sum*int(n)
                    return sum*int(n)
            grid_no += 1
    return -1

def findLoser(grids, nums):
    for n in nums:
        grid_no = 0
        to_skip = []
        for g in grids:
            if n in g.num_grid:
                row_num, col_num = g.num_grid[n]
                g.cleared[("row", row_num)] += 1
                g.cleared[("col", col_num)] += 1
                del g.num_grid[n]


                if g.cleared["row", row_num] == 5 or g.cleared["col", col_num] == 5:
                    if len(to_skip) == len(grids) - 1:
                        print "loser grid: ", grid_no

                        sum = 0
                        for key in g.num_grid:
                            sum += int(key)
                        print "winning number ",  n
                        print "sum ", sum 
                        print "answer ",  sum*int(n)
                        return sum*int(n)
                    else:
                        print "grid no: ", grid_no, " won"
                        to_skip.append(g)
            grid_no += 1
        for w in to_skip:
            grids.remove(w)
    return -1

if __name__=="__main__":
    with open("input4.txt", 'r') as f:
        input = f.read()
        input_vec = input.split("\n\n")
        bingo_nums = input_vec[0]
        nums = bingo_nums.split(',')

        grids = []
        for grid_str in input_vec[1:]:
            grid = Grid(5, 5)
            rows = grid_str.split('\n')
            row_num = 0
            col_num = 0
            for row_num, row in enumerate(rows):
                cols = [c for c in row.split(" ") if c]
                for col_num, c in enumerate(cols):   
                    grid.num_grid[c] = (row_num, col_num)
            grids.append(grid)
    findWinner(grids, nums)
    findLoser(grids, nums)







