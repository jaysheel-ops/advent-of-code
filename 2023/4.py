import sys
D = open("input.in").read().strip()
wnum = []
ynum = []
s1 = 0
s2 = 0
copies = {}
total_cards = len(D.split("\n"))
cardno = 1
print(total_cards)
for no in range(total_cards):
    copies[no+1] =  1
for line in D.split("\n"):
    cards = line.split(":")
    winning = cards[1].split("|")[0].strip()
    winning = [int(c) for c in winning.split()]
    your = cards[1].split("|")[1].strip()
    your = [int(c) for c in your.split()]
    
    tempsum = 0
    for i in your:
        if i in winning:
            tempsum+=1
            print('tempsum', tempsum)
    
    print(cardno)
    for i in range(cardno+1, 1+cardno+tempsum):
        if cardno == 1:
            print('copies of 1', copies[i])
        copies[i] += copies[cardno] 
        if cardno == 4:
            print('copies of 4 ', copies[i])
        
    cardno+=1


    
for key, value in copies.items():
    print("Key ", key, "value ", value)
    s2+=value
print(s2)
    # s1
    # for i in winning: 
    #     if i in your:
    #         if tempsum == 0:
    #             tempsum=1
    #         else:
    #             tempsum*=2

    # s1 += tempsum



        
