class Cal(object):

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def set_number(self,A,B):
        self.B1 = (self.B % 10)
        self.B2 = self.B & 100 - self.B1
        self.B3 = (self.B // 100)*100

    def print_number():
        print(A*B1)
        print(A*B2)
        print(A*B3)

    def get_number():
        A,B = map(int,input().split())
        return A,B

class Cal() = c1()
c1.get_number()
