numbers = []

A,B,C = map(int,input().split())
numbers.append(A)
numbers.append(B)
numbers.append(C)
numbers.sort()

print(numbers[1])
