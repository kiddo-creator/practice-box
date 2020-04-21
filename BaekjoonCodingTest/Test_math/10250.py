T = int(input())
# T:testtime

for i in range(T):
    H,W,N = map(int,input().split())
    #H:high , W:wide , N:number
    if(N<=H):
        print("%d01" % N)
    else:
        H_num = N%H
        W_num = (N//H)+1
        if H_num == 0:
            H_num=H
            W_num=W_num-1
        else:
            pass
        if(W_num<10):
            print("%d0%d" % (H_num,W_num))
        else:
            print("%d%d"  % (H_num,W_num))
