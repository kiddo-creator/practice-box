wide, high = map(int,input().split())

arr=[[i]*2 if i%2==0 else i+10 for i in range(0,wide)]
print(arr)
