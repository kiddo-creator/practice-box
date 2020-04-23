T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    result = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    if r1 > result + r2 or r2 > result + r1 or result > r1 + r2:
        print(0)
    elif r1 == result + r2 or r2 == result + r1 or r1 + r2 == result:
        print(1)
    else:
        print(2)
