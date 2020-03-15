a = int(input())
s = input().strip() # 공백 문자 제거
num = [int(c) for c in s]

def print_number():
    b1=(a*num[2])
    b2=(a*num[1])
    b3=(a*num[0])
    b4=(a*num[2])+(a*num[1]*10)+(a*num[0]*100)
    
    print(b1)
    print(b2)
    print(b3)
    print(b4)

print_number()
