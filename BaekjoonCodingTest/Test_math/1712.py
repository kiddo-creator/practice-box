A, B, C = map(int, input().split())
if (C <= B):
    be_point = -1
else:
    be_point = A//(C-B) +1
print(be_point)
