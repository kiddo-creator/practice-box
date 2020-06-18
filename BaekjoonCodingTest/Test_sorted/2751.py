#받은값들을 절반으로 나눠서 인덱스가 낮은값부터 순서대로 비교해서 합친다.
#문제버젼 말고 정렬까지 하는걸로

arr = [8,4,5,3,1,6,7,2] # 담을 리스트

def merge_sort(arr):
    print("in merge_Sort!")
    if len(arr) == 1:
        print("return merge is 1" , arr)
        return arr

    pivot = int(len(arr)/2)

    arr1,arr2=arr[:pivot],arr[pivot:]
    arr1,arr2=merge_sort(arr1), merge_sort(arr2)

    print(arr1)
    print(arr2)

    arr_merge=list()

    i,j=0,0

    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            arr_merge.append(arr2[j])
            j=j+1
        else:
            arr_merge.append(arr1[i])
            i=i+1

    arr_merge.extend(arr1[i:])
    arr_merge.extend(arr2[j:])

    print("return merge", arr_merge)
    return arr_merge

print(merge_sort(arr))
