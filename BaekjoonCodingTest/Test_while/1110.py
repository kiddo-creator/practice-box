num = str(input()) # num 값
cycle = 0 # cycle 횟수

if int(num) < 10: # num이 한자릿수일때 두자릿수로 만들기
    num = "0" + num  # num 'str'

new = num # new 정의

 #루프시작
while True:
    a = int(new[0]) + int(new[1])
    a = str(a)

    if int(a)<10: #합이 10 보다 작을경우
        new = new[1] + str(a)

    else: #합이 10보다 클경우
        new = new[1] + a[1]

    if new == num: # 탈출
        print(cycle+1, end="")
        break

    else: #싸이클 횟수추가
        cycle += 1
