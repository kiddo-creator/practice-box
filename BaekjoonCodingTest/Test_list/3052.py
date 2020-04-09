num=[]
for i in range(0,10):
    a=int(input())
    a=a%42
    num.append(a)

result = len(set(num))
print(result)
