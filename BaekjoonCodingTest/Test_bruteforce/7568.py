# 이중리스트로 <<키,몸무게> * N명>으로 풀기
size = int(input())
arr=list()

for i in range(size):
    data = list(map(int,input().split()))
    arr.append(data)

tall=0
weight=0
rank=0

while(True):
    max_tall=max(arr[0][0],arr[len(arr)-1][0])
    for i in len(arr):
        if arr[]

#몸무게따로 키따로
# n = int(input())
# weight, high = []*n, []*n
# rank =
# for i in len(n):
#     weight[i], high[i] = map(int,input().split())

##답
# num_student = int(input())
# student_list = []
#
# for _ in range(num_student):
#     weight, height = map(int, input().split())
#     student_list.append((weight, height))
#
# for i in student_list:
#     rank = 1
#     for j in student_list:
#         if i[0] < j[0] and i[1] < j[1]:
#                 rank += 1
#     print(rank, end = " ")
