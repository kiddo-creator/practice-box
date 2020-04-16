Testcase = int(input())
s_arr=[]

for i in range(20):
    s_arr.append(i)


for i in range(Testcase):
    a, b =map(str,input().split())
    for j in b:
        print(j*int(a),end="")
    print()


# 끝을 이여서 출력하는 end메소든
