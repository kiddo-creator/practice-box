n=str(input())

def maker(n):
    sum=0
    for i in n:
        sum=sum+int(i)
    print(sum)
    return maker(int(n)+sum)

maker(n)
range(-1,-1,-1)
# n="안녕"
#
# for i in n:
