# part 1:
# import sys
# D = open(sys.argv[1]).read().strip()
# gmaes = {}
# solution = []
# constraint = {'red': 12 , 'green': 13  , 'blue': 14  }
# i = 1;
# for line in D.split("\n"):
#     add = 1
    
#     temp = line.split(":")
#     temp[0], temp[1] = temp[0].strip(),temp[1].strip()
#     sets = temp[1].split(";")
#     for set in sets:
#         color = {}
#         parts = set.split(",")
#         for part in parts: 
#             val, col = part.split()
#             if col in color.keys():
#                 color[col] += int(val)
#             else:
#                 color[col] = int(val)

#         for key, value in color.items():
#             if constraint[key]<color[key]:
#                 add = 0
        
#     if add:
#         print(i)
#         solution.append(i)


        
#     i+=1
# print(sum(solution))

# Part 2:
import sys
import numpy as np
D = open(sys.argv[1]).read().strip()
gmaes = {}
solution = []
constraint = {'red': 12 , 'green': 13  , 'blue': 14  }
power = 0
i = 1;
for line in D.split("\n"):
    add = 1
    game_max = {}
    temp = line.split(":")
    temp[0], temp[1] = temp[0].strip(),temp[1].strip()
    sets = temp[1].split(";")
    for set in sets:
        color = {}
        parts = set.split(",")
        for part in parts: 
            val, col = part.split()
            if col in game_max.keys():
                if game_max[col] < int(val):
                    game_max[col] = int(val)
            else:
                game_max[col] = int(val)

    sum_m = [val for val in game_max.values()]
    sum_m = np.prod(sum_m)

    power += sum_m
    for key, value in color.items():
        if constraint[key]<color[key]:
            add = 0
    
    print(game_max)
        
    print(f'Game {i}: Power {power}')
    if add:
        solution.append(i)

    i+=1
print(power)