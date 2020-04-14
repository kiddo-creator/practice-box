import sys

N = int(sys.stdin.readline())
list1=[0]*N

for x in list1:
    x = str(sys.stdin.readline())
    idx = 0
    sum1 = 0
    for a in x:
        if a == 'O':
            sum1 += (idx+1)
            idx += 1
        else:
            idx = 0
    print(sum1)
