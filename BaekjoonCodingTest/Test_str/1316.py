testcase = int(input())
groupword = 0

for i in range(testcase):
    check = input()
    for j in check:
        for l in check:
            if j==l:
                if abs(check.index(j)-check.index(l)) > 1:
                    groupword = groupword+1
                    pass
                else:
                    pass
            else:
                pass

print(testcase-groupword)