arr = list(map(str, input().split()))
ans = list()
max = -1
cnti = 0
for i in arr:
    cnt = 0
    for k in i:
        cnt = int(k) + cnt
    ans.append(cnt)

for i in ans:
    if i > max:
        max = i
        cnti=cnti+1

print(arr[cnti-1])