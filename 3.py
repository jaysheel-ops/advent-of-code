import sys
D = open("input.in").read().strip()
sym = '-+/*&@#$%='
lines = []
for line in D.split("\n"):
    lines.append(line)
    # pass

numloc = {}
symloc = []
solution = []
# store all locations of symbols
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in sym:
            symloc.append(f'{i}{j}')

for i in range(len(lines)):
    start = -1
    end = -1
    line = i
    add = 0
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            if start == -1:
                start = j
            else:
                end = j
        elif lines[i][j] == '.' or lines[i][j] in sym:
            if start != -1:
                end = j
                numloc[f'{i}{j}'] = {}
                numloc[f'{i}{j}']['s'] = start
                numloc[f'{i}{j}']['e'] = end
                numloc[f'{i}{j}']['i'] = line
                numloc[f'{i}{j}']['val'] = lines[i][start:end]
                start = -1
                end = -1

for key,value in numloc.items():
    start = int(value['s'])
    end = int(value['e'])
    i = value['i']
    length = len(lines[0])
    val = int(lines[i][int(start):end])
    if i == 0:
        if start == 0:
            temp_arr1 = lines[i+1][start:min(end+1, length)]
            temp_arr2 = lines[i][start:min(end+1, length)]
            for k in sym:
                if k in temp_arr1 or k in temp_arr2:
                    solution.append(val)
                    break
        elif start!=0:
            temp_arr1 = lines[1+1][start-1:min(end+1, length)]
            temp_arr2 = lines[1][start-1:min(end+1, length)]

            for k in sym:
                if k in temp_arr1 or k in temp_arr2:
                    solution.append(val)
                    break
    elif i < len(lines)-1:
        if start == 0:
            temp_arr1 = lines[i][start:min(end+1, length)]
            temp_arr2 = lines[i-1][start:min(end+1, length)]
            temp_arr3 = lines[i+1][start:min(end+1, length)]
            for k in sym:
                if k in temp_arr1 or k in temp_arr2 or k in temp_arr3:
                    solution.append(val)
                    break
        elif start!=0:
            
            temp_arr1 = lines[i+1][start-1:min(end+1, length)]
            temp_arr2 = lines[i][start-1:min(end+1, length)]
            temp_arr3 = lines[i-1][start-1:min(end+1, length)]

            for k in sym:
                if k in temp_arr1 or k in temp_arr2 or k in temp_arr3:
                    solution.append(val)
                    break
    elif i == len(lines)-1:
        if start == 0:
            temp_arr1 = lines[i][start:min(end+1, length)]
            temp_arr2 = lines[i-1][start:min(end+1, length)]
            for k in sym:
                if k in temp_arr1 or k in temp_arr2:
                    solution.append(val)
                    break
        elif start!=0:
            temp_arr1 = lines[i-1][start-1:min(end+1, length)]
            temp_arr2 = lines[i][start-1:min(end+1, length)]
            for k in sym:
                if k in temp_arr1 or k in temp_arr2:
                    solution.append(val)
                    break

print(sum(solution))