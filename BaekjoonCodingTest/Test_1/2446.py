#모래시계 모양 별찍기
#20.04.03

Test_case = int(input())
Lines = Test_case*2-1
for i in range(0,Test_case-1):
    up_star_print = int(Lines-(2*i))*"*"
    print("%s%s" % (" "*i,up_star_print))

for i in range(1,Test_case+1):
    down_star_print = int(2*i-1)*"*"
    down_pace = Test_case-i
    print("%s%s" % (" "*down_pace,down_star_print))
