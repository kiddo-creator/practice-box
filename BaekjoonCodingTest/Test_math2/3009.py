arr_x=list()
arr_y=list()

for i in range(3):
    x,y = map(int,input().split())
    arr_x.append(x)
    arr_y.append(y)

arr_x.sort()
arr_y.sort()
ans_x=0
ans_y=0

if arr_x[0]==arr_x[1]:
    ans_x=arr_x[2]
elif arr_x[1]==arr_x[2]:
    ans_x=arr_x[0]
else:
    pass

if arr_y[0]==arr_y[1]:
    ans_y=arr_y[2]
elif arr_y[1]==arr_y[2]:
    ans_y=arr_y[0]
else:
    pass

print(ans_x,ans_y)
