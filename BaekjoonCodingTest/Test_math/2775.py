apart = [[0]*15 for i in range(15)]

for i in range(15):
    apart[0][i]=i
    apart[i][0]=0

for j in range(1,15):
    for k in range(1,15):
        apart[j][k]=apart[j-1][k]+apart[j][k-1]

T=int(input())
for i in range(T):
    a = int(input())
    b = int(input())
    print(apart[int(a)][int(b)])
