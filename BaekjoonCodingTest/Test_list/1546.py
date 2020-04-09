import sys

a=int(input())
l=[0]*a
l=list(map(int,input().split()))
print(l[1])
max=0
sum=0

for i in range(len(l)):
    if max<int(l[i]):
        max=int(l[i])

for i in range(len(l)):
    l[i] = int(l[i])/max*100
    sum = sum + int(l[i])
ans = int(sum/len[i])
print(ans)
