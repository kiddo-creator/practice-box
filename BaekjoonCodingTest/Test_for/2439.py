Test_Case = int(input())

for numbers in range(1,Test_Case+1):
    blank = Test_Case - numbers
    blank_space = blank*" "
    star_space = numbers*"*"
    print("%s%s" % (blank_space,star_space))
