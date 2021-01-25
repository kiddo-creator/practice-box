num = int(input())
ans_list = list(map(int,input().split()))

total_score=0
score=0

for i in range(len(ans_list)):
    if ans_list[i] == 0:
        score=0
        pass
    else:
        score=score+1
        total_score=total_score+score

print(total_score)
