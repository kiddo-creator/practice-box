dn_case = int(input())
up_case = int(input())

# 범위설정
arr=list(range(dn_case,up_case+1))
new_arr=[]

#소수판별
for i in arr:
    if i==1:
        del arr[0]
    else:
        temp_num=2
        while (temp_num < i):
            # 자신 보다 작은수로 나눠지면, 소수로 취급하지 않음
            if (i % temp_num) == 0:
                new_arr.append(i)
                break
            else:
                temp_num =temp_num + 1

#소수 new_arr
new_arr=set(arr)-set(new_arr)

#합 구하기
sum=0
for i in new_arr:
    sum=i+sum

#최소값 구하기
min=10000
for i in new_arr:
    if i<min:
        min=i

#결과 출력
if sum==0 and min==10000:
    print(-1)
else:
    print(sum)
    print(min)
