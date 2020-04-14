c=int(input())

stu=[]

avglist=[]

for i in range(c): ## 테스트 케이스의 횟수만큼 반복
    a=list(map(int,input().split()))
    stu.append(a) ## 학생 수와 성적을 2차원 배열로
    sum1=sum(stu[i][1:])  ## 학생들의 점수 합

    avg=sum1/stu[i][0] ## 학생들의 점수 평균
    avglist.append(avg) ## 학생들의 점수 평균 리스트

    cnt=0
    for k in range(stu[i][0]):
        if stu[i][k+1]>avglist[i]:
            cnt+=1
    rate=100*cnt/stu[i][0]
    print('%.3f%%' % rate)
