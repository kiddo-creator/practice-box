# 주사위게임
# 규칙 1. 같은눈 3개나오면 10,000+같은눈x1,000
# 규칙 2. 같은눈 2개나오면 10,000+같은눈x100
# 규칙 3. 모두 다른 눈 가장큰눈x100

player = int(input())
dice = list()
result = list()

for i in range(player):
    dice.append(map(list,input().split()))

for i in range(player):
    if dice[i][0] == dice[i][1] == dice[i][2]:
        result.append(10000+int(dice[i][0])*1000)
    elif dice[i][0] != dice[i][1] != dice[i][2]:
        max=0
        for k in dice[i]:
            if dice[i][k]>max:
                max = dice[i][k]
            result.append(int(max)*100)
    else:
        flag=0
        if dice[i][0]==dice[i][1]:
            result.append(10000+int(dice[i][0])*100)
        else:
            result.append(10000+int(dice[i][2])*100)
print(result.max)