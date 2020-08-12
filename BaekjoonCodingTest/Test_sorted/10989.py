# counting sort
Testcase = int(input())
non_arr=[0]*10001
arr=list()

#non_arr에 인덱스에 상수를 input
for k in range(Testcase):
    a=int(input())
    non_arr[a]=non_arr[a]+1

index=0
#non_arr인덱스에 순차적으로 들어가면서 값이 쌓인 횟수만큼 출력
for i in non_arr:
    if i==0:
        pass
    else:
        for k in range(i):
            print(non_arr[index])
    index=index+1