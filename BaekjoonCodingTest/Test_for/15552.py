import sys

time = int(input())

for i in range(0,time):
    A,B =  map(int,sys.stdin.readline().split(' '))
    print(A+B)
