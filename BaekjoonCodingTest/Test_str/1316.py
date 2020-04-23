testcase=int(input())
for i in range(testcase):
    alp=input()
    cnt=0
    for x in range(len(alp)):
        if len(alp)==1:
            cnt=cnt+1
        else:
            alp.find(x)
