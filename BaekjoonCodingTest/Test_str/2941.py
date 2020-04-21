x = input()
d = len(x)
i = 0
while (i<len(x)):
    if x[i] != x[-1]:
        if x[i] == 'd':
            if len(x[i:]) >= 3:
                if x[i+1] == 'z' and x[i+2] == '=':
                    i += 2
                    d -= 2

        if x[i] == 'c' or x[i] == 's' or x[i] == 'z':
            if x[i+1] == '=':
                i += 1
                d -= 1

        if x[i] == 'c' or x[i] == 'd':
            if x[i+1] == '-':
                i += 1
                d -= 1

        if x[i] == 'l':
            if x[i+1] == 'j':
                i += 1
                d -= 1

    i += 1
print(d)
