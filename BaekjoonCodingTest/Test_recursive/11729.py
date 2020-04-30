def Hanoi(n,start,tempt,end):
    if n==1:
        print(start,end)
    else:
        Hanoi(n-1,start,end,tempt)
        Hanoi(1,start,tempt,end)
        Hanoi(n-1,tempt,start,end)
        return

n=int(input())
print(2**n-1)
Hanoi(n,1,2,3)
