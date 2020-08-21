# n, m = map(int, input().split())
# arr = list([0] * 2)
# new_arr= list([0] * 2)
#
# for i in range(1,n+1):
#     for a in range(1,m+1):
#         arr.append(i + a)
#
# for i in range(2,n+m+1):
#     if i == 0:
#         pass
#     else:
#         flag = arr.count(i)
#         new_arr.append(flag)
#
# num = int(input())
#
# print("num : %f" % ((int(arr.count(num))/n*m)))

n,m = map(int,input().split())
cnt=[0]*(n+m+3)
max=0

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]= cnt[i+j]+1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
