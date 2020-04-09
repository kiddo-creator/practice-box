arr = []

for i in range(9):
    number = int(input())
    arr.append(number)

print(max(arr))
print(arr.index((max(arr)))+1)
