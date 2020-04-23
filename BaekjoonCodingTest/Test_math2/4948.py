import math

while True:
    num=int(input())
    if num==0:
        break
    elif num ==1:
        print(1)
    else:
        arr=list(range(num+1,2*num+1))
        new_arr=list()
        for i in arr:
            temp_num=2
            sqrt_i=math.sqrt(i)
            while sqrt_i>=temp_num:
                if num % temp_num==0:
                    print(i,"bye")
                    new_arr.append(i)
                    break
                else:
                    temp_num=temp_num+1
                    # print(i,"hi")
