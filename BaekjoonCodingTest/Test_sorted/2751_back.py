# 머지소트 백준 2751번

testcase = int(input())
arr = list()

for i in range(testcase):
    k = int(input())
    arr.append(k)

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    pivot = int(len(arr)/2)

    arr1,arr2=arr[:pivot],arr[pivot:]
    arr1,arr2=merge_sort(arr1), merge_sort(arr2)

    arr_merge=list()

    i,j=0,0

    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            arr_merge.append(arr1[i])
            i=i+1
        else:
            arr_merge.append(arr2[j])
            j=j+1

    arr_merge.extend(arr1[i:])
    arr_merge.extend(arr2[j:])

    return arr_merge

for i in merge_sort(arr):
    print(i)
