# n=int(input()) #n 번째 수
#
# ans=0 # n번수의 값
# i=0  # 반복인자
#
# while True:
#     k=i*(i+1)/2 # 가로 첫째줄 기준 i에 대한번호
#     if n==k:
#         print(i)
#         break
#     elif k<n:
#         i=i+1
#     elif k>n:
#         a=k-n#만큼 남아
#         ans =(i-a)/(1+a)
#         print(ans)
#         break

n = int(input()) # n번째수

group_num = 0
num = 0

while num < n :
    group_num = group_num + 1
    num = num + group_num

# 1,1
# 2,3
# 3,6
# 4,10

if num == n:
     print("1/%d" & (1/group_num))

elif group_num % 2 == 0:
    top = group_num -
