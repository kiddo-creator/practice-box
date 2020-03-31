Test_Case = int(input())

for numbers in range(Test_Case):
    A,B = map(int,input().split())
    print("Case #%d: %d" % (numbers+1,A+B))
