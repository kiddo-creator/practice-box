dog = [0,2,2,6,5,6,3,0,8,2]
print(dog)
n = len(dog)
fox = []

for x in range(n):
    wolf=[]
    cat = -1

    for i in dog:
        if cat == -1:
            cat = i
        else:
            if i < cat:
                cat=i

    for j in dog:
        if j == cat:
            fox += [j]
        else:
            wolf += [j]

    dog = wolf

sortResult = fox
print(sortResult)