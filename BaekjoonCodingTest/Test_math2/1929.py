M, N = map(int, input().split())
x = [0, 0]+[1]*(N-1)

for i in range(2, N+1):
    if x[i] and i >= M: print(i)
    for j in range(2*i, N+1, i): x[j]=0
