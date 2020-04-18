import math

A,B,V = map(int,input().split())
# 올라가는높이 A, 떨어지는 높이 B,막대 높이 V

day =math.ceil((V-A)/(A-B)) #걸린 날
print(day+1)
