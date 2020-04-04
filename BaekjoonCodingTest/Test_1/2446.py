#모래시계 모양 별찍기
#20.04.03

Test_case = int(input())
Lines = Test_case*2-1

T_space = Test_case*2
L_space = ""
R_space = ""

for i in range(1,Test_case):
    print(L_space*i,"*"*T_space-2*i,R_space*i)
