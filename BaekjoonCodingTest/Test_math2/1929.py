import math
# math import

dw_case, up_case = map(int,input().split())
arr=list(range(dw_case,up_case+1))
new_arr=list()
#dw_case,up_case arr범위 설정 // new_arr리스트

for i in arr:
    if i==1: # 1은 소수가 아닙니다.
        del arr[0]
    else:
        sqrt_i = math.sqrt(i)
        temp_num = 2
        while temp_num<=sqrt_i:
            if i%temp_num==0:
                new_arr.append(i)
                break
            else:
                temp_num=temp_num+1

set(arr)
set(new_arr)
print(arr-new_arr)
