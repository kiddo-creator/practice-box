test_cnt = int(input())
result = test_cnt #입력한 숫자의 개수 만큼 받음

num_list = list(map(int, input().split()))

for num in num_list:
    temp_num = 2
    # 1을 소수로 취급하지 않음.

    if (num == 1):
        result -= 1
    else:
        # 소수 검사
        while (temp_num < num):
            # 자신 보다 작은수로 나눠지면, 소수로 취급하지 않음
            if (num % temp_num) == 0:
                result -=1
                break
            else:
                temp_num += 1
print(result)
