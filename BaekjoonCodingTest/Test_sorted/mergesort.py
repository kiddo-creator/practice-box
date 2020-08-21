
import random
#version 1 : random array
arr = [ random.randint(1,50) for i in range(8) ]


#version 2 : read csv
# import pandas
#
# temp = pandas.read_csv('bubblesort_data.csv', header = None)
# temp = temp.transpose()
# temp_columns = len(temp)
# temp_rows = len(temp.transpose())
#
# #arr = [ random.randint(1, 20) for i in range(temp_columns + temp_rows) ]
# arr=[]
# for x in range(temp_rows):
#     for y in range(temp_columns):
#         arr.append(int(temp[x][y]))a


#arr pivot

pivot = int(len(arr)/2)

arr1 = arr[:pivot]
arr2 = arr[pivot:]

#merge sort Main code

def merge_sort(arr):
    print("in merge_sort")
    if len(arr) == 1:
        print("return merge is 1 ", arr)
        return arr

    pivot = int(len(arr)/2)

    arr1, arr2 = arr[:pivot], arr[pivot:]
    arr1, arr2 = merge_sort(arr1), merge_sort(arr2)

    print(arr1)
    print(arr2)

    arr_merge = list()

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr_merge.append(arr2[j])
            j+=1
        else:
            arr_merge.append(arr1[i])
            i+=1

    arr_merge.extend(arr1[i:])
    arr_merge.extend(arr2[j:])

    print("return merge", arr_merge)
    return arr_merge