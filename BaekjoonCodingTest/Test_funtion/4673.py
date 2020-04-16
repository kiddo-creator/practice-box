def self_num():
    no_s_sum=set()
    for i in range(1,10001):
        a=i
        for j in str(a):
            a=a+int(j)
        no_s_sum.add(a)
    for j in range(1,10001):
        if not j in no_s_sum:
            print(j)

self_num()
