# 입력받을횟수를 정한다
# 정렬되지 않는 non_arr 값중 최솟값을 flag에 넣음
# flag값을 하나씩 arr에 추가함
# flag값을 제외한걸 non_arr로 제설정


num = int(input()) #입력받을 횟수설정
non_arr = [] #정렬되지 않는 리스트생성
arr = [] #정렬값을 담을 리스트 생성
new_arr = [] #정렬된값을 제외한 나머지 값을 담을 리스트 생성

for i in range(num): #정렬되지않는 리스트 non_arr
    k = int(input())
    non_arr.append(k)

for i in non_arr:
    sample = -1

    for j in non_arr: #최소값 flag에 넣기
        if sample == -1:
            sample = j
        else:
            if sample > j:
                sample = j

    for m in non_arr: #flag값 arr추가 및 정렬되지않은값 non_arr에 다시담기
        if m == sample:
            arr.append(m)
        else:
            new_arr.append(m)

    non_arr = new_arr
    new_arr = []

print(arr)





