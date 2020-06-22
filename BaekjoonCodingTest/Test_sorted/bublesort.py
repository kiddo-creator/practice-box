
arr = [0,2,2,6,5,6,3,0,8,2]
print("check your arr",arr)
n = len(arr)
arr_sort = []

for x in range(n):
    new_arr=[]
    flag = -1

    for i in arr:
        if flag == -1:
            flag = i
        else:
            if i < flag:
                flag=i

    for j in arr:
        if j == flag:
            arr_sort += [j]
        else:
            new_arr += [j]

    arr = new_arr

sortResult = arr_sort
print(sortResult)
