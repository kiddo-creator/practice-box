word = input()
listn = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for k in listn:
    word = word.replace(k, '*')

print(len(word))
