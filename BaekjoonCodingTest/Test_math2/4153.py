while True:
    #변수선언, 결과값초기화
    x, y, z =map(int,input().split())
    ans=""

    #0 0 0이면 탈출
    if x==0 and y==0 and z==0:
        break
    #직각삼각형의 조건
    elif x**2+y**2==z**2 or x**2+z**2==y**2 or z**2+y**2==x**2:
        ans="right"
    else:
        ans="wrong"

    #출력
    print(ans)
