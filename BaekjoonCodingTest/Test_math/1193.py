n=int(input()) #n 번째 수

ans=0 # n번수의 값
i=0  # 반복인자

while True:
    k=i*(i+1)/2 # 가로 첫째줄 기준 i에 대한번호
    if n==k:
        print(i)
        break
    elif k<n:
        i=i+1
    elif k>n:
        a=k-n#만큼 남아
        ans =(i-a)/(1+a)
        print(ans)
        break
