lines = int(input())

for i in range(lines):
    str = input()
    if lines == len(str):
        print("#%d YES" % (i+1))
    else:
        print("#%d NO" % (i+1))
