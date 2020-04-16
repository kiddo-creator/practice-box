arr = []
sum = 0

for i in range(1001):
    a=i
    arr.append(a)

n=input()

if int(n)<100:
    print(n)
elif 100<=int(n)<1000:
    for i in str(n):
        if int(n[i])-int(n[i+1])==int(n[i+1])-int(n[i+2]):
            sum = sum +1
    print(int(n)+int(sum))
