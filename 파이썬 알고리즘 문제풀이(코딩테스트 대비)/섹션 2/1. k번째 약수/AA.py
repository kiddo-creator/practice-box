# k번째 약수
#n, k = map(int, input().split())
list = list()

for i in range(1,n+1):
    if n % i == 0:
        list.append(i)
    else:
        pass

if len(list) < k:
    print(-1)
else:
    print(list[k-1])
