Card_num , sum = map(int,input().split())
Card_list=list(map(int,input().split()))
Sum_list=list()

for i in Card_list:
    for j in Card_list:
        for k in Card_list:
            if i==j or j==k or i==k:
                pass
            else:
                Sum_list.append(i+(j)+(k))

flag=0
Sum_list.sort()

for i in Sum_list:
    if i>sum:
        flag=Sum_list.index(i)
        break
    else:
        pass
print(Sum_list[flag-1])
