S = input()
atoz = "abcdefghijklmnopqrstuvwxyz"

s_arr=[]
a_to_z=[]
ans_arr=[]
for i in S:
    s_arr.append(i) # s_arr 정의
for i in atoz:
    a_to_z.append(i)# a_to_z 정의
for i in range(len(a_to_z)): #ans_arr정의
    ans_arr.append(i)

for j in range(0,len(a_to_z)): #다중반복 중복단어판별
    for i in range(0,len(S)):
        if S[i]==a_to_z[j]:
            ans_arr[j]=s_arr.index(S[i])
            break
        else:
            ans_arr[j]="-1"
for i in range(len(ans_arr)):
    print(ans_arr[i],end=' ')
