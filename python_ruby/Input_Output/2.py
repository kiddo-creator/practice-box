in_str = input(" 아이디를 입력해주세요. \n")

# print(type(in_str))

real_egoing = "11"

# 11로 입력할시 str인 11과 int형인 11이 다르게 출력됨
# 11로 입력했을때 바로 출력되기위해서는 형변환을 해야함.

real_k8805 = "ab"

if real_egoing == in_str:
    print("Hello, egoing! ")
elif real_k8805 == in_str:
    print("Hello, k8805! ")
else:
    print("Who are you ?")
