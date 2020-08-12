# k번째 약수
n, k = map(int, input().split())
arr = list()

for i in range(1, n + 1):
    if n % i == 0:
        arr.append(i)
    else:
        pass

if len(arr) < k:
    print(-1)
else:
    print(arr[k - 1])
