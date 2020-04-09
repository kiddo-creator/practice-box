Test_case = int(input())
Test_time = int(Test_case+1) // 2

if Test_case==1:
    print("*")
else:
    for i in range(1,Test_case*2+1):
        if  i % 2 !=0:
            print("%s" % ("* "*int(Test_time)))
        else:
            print("%s" % (" *"*int(Test_time)))
