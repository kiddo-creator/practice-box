a = int(input())
b = list(map(int, input().split()))

max = -1000000
min = 1000000

for i in range(a):
    if b[i] >= max:
        max = b[i]
    if b[i] <= min:
        min = b[i]

print("%d %d" % (min,max))
