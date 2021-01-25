# 인프런 강의
textlist = list(range(21))

for _ in range(10):
    s,e = map(int,input().split())
    for i in range((e-s+1)//2):
        textlist[s+i], textlist[e-i]=textlist[e-i], textlist[s+i]

textlist.pop(0)

for x in textlist:
    print(x,end = ' ')
    
# 내가 푼
# textlist = list(range(1,21))
# emptylist = list()
# cnt=0
#
# for i in range(10):
#     sector_a,sector_b = map(int,input().split())
#
#     for a in textlist:
#         if int(a) < sector_a:
#             emptylist.append(a)
#         elif sector_a <= int(a) <= sector_b:
#             if cnt==0:
#                 for rev in textlist[sector_a:sector_b:-1]:
#                     emptylist.append(rev)
#                     cnt=cnt+1
#             else:
#                 pass
#         else:
#             emptylist.append(a)
#     if i!=9:
#         textlist=emptylist
#         emptylist=list()
#         cnt=0
#
# print(textlist)
