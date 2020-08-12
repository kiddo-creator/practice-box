Testcase = int(input())
non_arr=[0]*10001
arr = []

for i in range(Testcase):
    a=int(input())
    non_arr[a]=non_arr[a]+1

for k in non_arr:
    if k != 0:
        flag=non_arr.index(k)
        if k > 1:
            for i in range(flag):
                print(flag)
        elif k==1:
            print(flag)
    else:
        pass