arr=list()

for i in int(input()):
    a=int(input())
    arr.append(a)

n = len(arr)
arr_sort = []

for x in range(n):
    new_arr=[]
    flag = 4001

    for i in arr:
        if flag == 4001:
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

def first():
    result=0
    for k in arr_sort:
        result=result+k
    return result/len(arr_sort)

def second():

