testcase = int(input())
num_list=list(map(int,input().split()))
ans_list=list()

def reverse(num_list):
    reverse_list=list()
    for k in num_list:
        reverse_list.append(str(k)[::-1])
    return reverse_list

def isPirme(reverse_list):
    cnt=0
    for i in reverse_list:
        for k in range(2,int(i)):
            if int(i)%k==0:
                cnt=cnt+1
                break
        if cnt==0:
            ans_list.append(int(i))
        cnt=0

    for i in ans_list:
        print(i)

isPirme(reverse(num_list))
