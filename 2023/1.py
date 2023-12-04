import sys
D = open(sys.argv[1]).read().strip()
ans = 0
word_dig = {'one': 1, 'two':2 , 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
for line in D.split('\n'):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, value in enumerate(['zero', 'one', 'two' , 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(value):
                digits.append(str(d))

    sum = int(digits[0] + digits[-1])
    ans += sum
print(ans)