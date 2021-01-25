fir_listsize=int(input())
fir_list = list(map(int,input().split()))

sec_listsize=int(input())
sec_list=list(map(int,input().split()))

sum_list=fir_list+sec_list
sum_list.sort()

print(sum_list)
