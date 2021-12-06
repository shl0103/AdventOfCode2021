from os import read

def fish_after_n_days(fish, days):
    fish_map = {}
    for i in range(0, 9):
        fish_map[i] = 0
    fish = [int(i) for i in fish]
    for f in fish:
        fish_map[f] += 1
    
    for n in range(days):
        ready_to_repro = fish_map[0]
        for i in range(0, 8):
            fish_map[i] = fish_map[i+1]      
        fish_map[6] += ready_to_repro
        fish_map[8] = ready_to_repro
    
    final_fish_count = 0
    for i in fish_map:
        final_fish_count += fish_map[i]
    print final_fish_count
    return final_fish_count

if __name__ == "__main__":
    fish = []
    with open("input6.txt", 'r') as f:
        input = f.read()
        fish = input.split(',')

    fish_after_n_days(fish, 256)
        