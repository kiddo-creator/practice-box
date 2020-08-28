a = int(input())
cnt=0
check_arr=list()

for i in range(2,a+1):
    cnt = 0
    for k in range(2,i):
        if i%k==0:
            cnt=cnt+1
            break

    if cnt==0:
         check_arr.append(i)
         pass

    cnt=0

print(len(check_arr))

# for i in check_arr:
#     print(i)


