Test = int(input())
lines = 2*Test-1
down_case = lines-Test

for i in range(1,Test):
    if i<Test:
        print("*"*i)
    elif i==Test:
        print("*"*Test)
    else:
        pass

for k in range(down_case+1):
    print("*"*(Test-k))
    if k==down_case+1:
        break
