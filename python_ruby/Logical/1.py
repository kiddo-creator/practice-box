str_id = input("아이디를 입력하세요.")
str_pw = input("패드를 입력하세요.")

real_id = "egoing"
real_pw = "1111"

if str_id == real_id:
    if str_pw == real_pw:
        print("hello, egoing!")
    else:
        print("wrong password")
else:
    print("wrong id")
