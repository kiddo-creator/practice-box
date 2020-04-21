dn_case = int(input())
up_case = int(input())

arr=[]

for x in range(dn_case,up_case):
    arr.append(x)

for i in arr:
    temp_num=2
    if i==1:
        del arr[0]
    if i<temp_num:
        if i%temp_num==0:
            del arr[arr.index(i)]
        else:
            temp_num=temp_num+1
    else:
        pass
sum=0
for i in arr:
    sum=i+sum

print(sum)
print(arr.min())
