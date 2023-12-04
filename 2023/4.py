import sys
D = open("input.in").read().strip()
wnum = []
ynum = []
s1 = 0
for line in D.split("\n"):
    cards = line.split(":")
    winning = cards[1].split("|")[0].strip()
    winning = [int(c) for c in winning.split()]
    your = cards[1].split("|")[1].strip()
    your = [int(c) for c in your.split()]
    
    tempsum = 0
    for i in winning: 
        if i in your:
            if tempsum == 0:
                tempsum=1
            else:
                tempsum*=2

    s1 += tempsum

print(s1)

        
