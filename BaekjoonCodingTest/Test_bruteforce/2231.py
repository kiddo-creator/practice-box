n = int(input())
num = n

start = max(n-len(str(n))*9,0)
ans = list()
for i in range(start,n):
    if num == sum(map(int,str(i)))+i:
        ans.append(i)
if len(ans) == 0 :
    print(0)
else :
    print(min(ans))
