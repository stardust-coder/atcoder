n = int(input())
s = input()
alist = list(map(int,input().split()))
basic = []
add = 0
for j in range(n):
    basic.append(add)
    if s[j] == "<":
        add += 1    
    else:
        add -= 1
basic.append(add)
minimum = min(basic)
newbasic = [val-minimum for val in basic]

def det(ls):
    res = True
    for i in range(n):
        if (ls[i] <= ls[i+1] and s[i] == ">") or (ls[i] >= ls[i+1] and s[i] == "<"):
            res = False
            break
    return res

k = 0
while True:
    #print("checl",alist,det(alist))
    if det(alist) == False:
        break
    #print("n",newbasic)
    for l in range(n+1):    
        alist[l] -= newbasic[l]
    k += 1

for t in range(n+1):    
    alist[t] += newbasic[t]

print(k)
print(" ".join(map(str,alist)))
for _ in range(k-1):
    print(" ".join(map(str,newbasic)))

#B
# n = int(input())
# alist = list(map(int,input().split()))
# tlist = [-k for k in alist]
# import heapq
# tak = 0
# aok = 0
# for _ in range(n):
#     heapq.heapify(tlist)
#     tak_add = heapq.heappop(tlist)
#     tak += tak_add
#     alist.remove(-tak_add)
#     #print(alist,tlist)
#     aok_add = alist.pop(int(len(alist)/2))
#     aok += aok_add
#     tlist.remove(-aok_add)
#     #print(alist,tlist)
# print(-tak)
# n = int(input())
# alist = list(map(int,input().split()))
# tlist = [-k for k in alist]
# li1 = [(i,alist[i]) for i in range(2*n)]
# slist = dict(li1)
# import heapq
# tak = 0
# aok = 0
# heapq.heapify(tlist)
# for _ in range(n):
#     tak_add = heapq.heappop(tlist)
#     tak += tak_add
#     key = [k for k, v in slist.items() if v == -tak_add][0]
#     slist.pop(key)
#     print(tlist,slist)
#     chuou = int(len(slist)/2)
#     aok_add = slist.pop(chuou)
#     aok += aok_add
#     tlist.remove(-aok_add)
#     print(tlist,slist)
# print(-tak)