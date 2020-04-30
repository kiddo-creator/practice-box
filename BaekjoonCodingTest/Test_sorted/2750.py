num = int(input())
arr = list()

for _ in range(num):
    arr.append(int(input()))

for i in range(num):
    for j in range(i+1,num):
        if arr[i]>arr[j]:
            flag = arr[j]
            arr[j] = arr[i]
            arr[i] = flag
        else:
            pass
# print(arr)

for _ in arr:
    print(_)
