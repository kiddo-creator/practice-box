#K번째 큰수

n,k = map(int,input().split())
arr=list(map(int,input().split()))
res=set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(arr[i]+arr[j]+arr[m])

res=list(res)
res.sort(reverse=True)
print(res[k-1])t