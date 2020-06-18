def fibonarchi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonarchi(n-1)+fibonarchi(n-2)

n=int(input())
print(fibonarchi(n))