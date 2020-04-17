a = int(input())
score_list = list(map(int, input().split()))
up = max(score_list)
result = 0

for i in range(0, a):
    score_list[i] = score_list[i]/up*100
    result = result + score_list[i]

result = result/a
print(result)
