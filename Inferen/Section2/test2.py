#k번째수

#T=Testcase 1<t<10
T=int(input())

#for range T
for t in range(T):
    n,s,e,k = map(int,input().split())
    arr=list(map(int,input().split()))
    arr=arr[s-1:e]
    arr.sort()

    print("#%d %d" %(t+1,arr[k-1]))

