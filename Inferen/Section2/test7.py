n= int(input())
cnt=0
cnta=list()

for i in range(1,n+1):
    for k in range(1,i):
        if k!=1 and i%k==0:
            cnt=cnt+1
            cnta.append(k)
            break
        else:
            pass
print(cnt)
