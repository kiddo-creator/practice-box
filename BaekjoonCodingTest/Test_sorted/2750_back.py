# 입력받을횟수를 정한다
# 정렬되지 않는 non_arr 값중 최솟값을 flag에 넣음
# flag값을 하나씩 arr에 추가함
# flag값을 제외한걸 non_arr로 제설정


num = int(input()) #입력받을 횟수설정
non_arr = [] #정렬되지 않는 리스트생성
new_arr = [] #정렬된값을 제외한 나머지 값을 담을 리스트 생성

for i in range(num): # non_arr 값 입력받기
    k = int(input())
    non_arr.append(k)

for i in non_arr:
    sample = -1001

    for j in non_arr: #최소값 flag에 넣기
        if sample == -1001:
            sample = j
        else:
            if sample > j:
                sample = j

    for m in non_arr: #flag값과 일치하는(=최솟값) 출력 및 정렬되지않은값 new_arr에 다시담기
        if m == sample:
            print(m)
        else:
            new_arr.append(m)

    non_arr = new_arr # 다시담은 new_arr를 기준으로 반복
    new_arr=[] #new _arr비워주기