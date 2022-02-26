# n = int(input())
# alist = list(map(int,input().split()))
# for i in range(int((n+1)/2)):
#     if alist[i] == alist[n-1-i]:
#         alist[i] = 0
#         alist[n-1-i] = 0

# ans = [x for x in alist if x != 0]
# s = set(ans)
# print(max(len(s)-1,0))
import math
l,r = map(int,input().split())

cl = [1,1]
for i in range(r):
    cl.append(int(i*(i-1)/2))


count = 0
for g in range(2,int(r/2)):
    small = math.ceil(l/g)
    big = math.floor(r/g)
    if big == 1:
        break
    print(g,small,big)
    if small == 1:
        small += 1
    count += cl[big-small+1]*2
    count += big-small + 1
print(count)