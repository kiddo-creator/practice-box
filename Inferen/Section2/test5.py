n, m = map(int, input().split())
arr = list([0] * 2)
new_arr= list([0] * 2)

for i in range(1,n+1):
    for a in range(1,m+1):
        arr.append(i + a)

for i in range(2,n+m+1):
    if i == 0:
        pass
    else:
        flag = arr.count(i)
        new_arr.append(flag)

num = int(input())

print("num : %f" % ((int(arr.count(num))/n*m)))
