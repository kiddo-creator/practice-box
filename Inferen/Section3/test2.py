testcase = input()
res=0
cnt=0

for i in testcase:
    if i.isdecimal():
        res=res*10+int(i)
for i in range(1,res+1):
    if res%i==0:
        cnt=cnt+1

print(cnt)
