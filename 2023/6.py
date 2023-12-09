import sys
D = open("input.in").read().strip()
time = []
dist = []
speed = -1
for line in D.split("\n"):
    # pass
    temp = line.split(":")
    if temp[0] == "Time":
        temp = temp[1].strip()
        time = [int(i) for i in temp.split()]
    else:
        temp = temp[1].strip()
        dist = [int(i) for i in temp.split()]
    
solution = []
for i in range(len(time)):
    solution.append(0)

for i in range(len(time)):
    best = dist[i] 
    for j in range(time[i]):
        speed = j
        nspeed = j*(time[i]-j)
        if nspeed > best:
            solution[i]+=1
        else:
            continue
    
import math
print(math.prod(solution))
    
now = 0
ntime = ""
ndist = ""
for i in dist: 
    ndist += str(i)
for i in time:
    ntime += str(i)
    
ntime = int(ntime)
ndist = int(ndist)

for i in range(ntime):
    speed = i
    nspeed = i*(ntime-i)
    if nspeed>ndist:
        now = ntime+1-(2*i)
        break

print(now)

    

        
