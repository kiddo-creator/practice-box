n_number =int(input())
array = list(map(int,input()))

sum=0
for i in range(len(array)):
    sum = array[i]+sum

print(sum)
