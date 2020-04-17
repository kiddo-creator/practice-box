alp = input()

atoz = "abcdefghijzlmnopqrstuvwxyz"
a_to_z=[]

ans=[]

for i in atoz:
    a_to_z.append(i)

for i in range(len(alp)):
    ans.append(i)

for i in range(len(alp)):
    for j in alp:
        if alp[i]==j:
            ans.append(alp[i])
            print(ans)
