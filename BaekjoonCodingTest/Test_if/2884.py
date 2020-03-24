H,M = map(int,input().split())

if 60>M>=45:
    print(H,M-45)
elif M<45:
    if H>=1:
        print(H-1,15+M)
    else:
        print(23,15+M)

# def set_time(H,M):
#     h=H-1
#     m=M-45
#     return print(h,m)
#
# set_time(H,M)
