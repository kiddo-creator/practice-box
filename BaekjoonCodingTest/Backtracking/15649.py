# check 리스트를 이용해 인덱스를 한칸씩 늘려간다
n, m = map(int, input().split())
check = [False] * (n + 1)
answer = [0] * m


def recusive(index, n, m):
    if index == m:
        for i in range(m):
            print(answer, end=' ')
        print()

        return

    for i in ragne(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        answer[index] = i
        recusive(index + 1, n, m)
        check[i] = False


recusive(0, n, m)
