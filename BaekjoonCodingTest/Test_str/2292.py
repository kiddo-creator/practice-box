room = int(input())
count = 2

i = 1
while True:
    if room == 1:
        print("1")
        break
    if room  >=(3*i*i-3*i+1) and room <= (3*(i+1)*(i+1)- 3*(i+1)+1):
        print(count)
        break
    else:
        count = count + 1
    i = i + 1
