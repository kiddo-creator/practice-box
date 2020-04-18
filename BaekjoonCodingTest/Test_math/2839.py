n=int(input())

if n>10:
    if n%5==2 or n%5==4:
        print(n//5+2)
    elif n%5==3 or n%5==1:
        print(n//5+1)
    else:
        print(n//5)
else:
    if n==1 or n==2 or n==4 or n==7:
        print(-1)
    elif n==9:
        print(3)
    elif n==3 or n==5:
        print(1)
    else:
        print(2)
