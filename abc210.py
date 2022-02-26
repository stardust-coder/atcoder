n,k = map(int,input().split())
clist = list(map(int,input().split()))

from collections import deque

q = deque()
for j in range(k):
    q.append(clist[j])

ans = 0
for i in range(n-k+1):
    #print(q)
    temp = len(set(q))
    if ans < temp:
        ans = temp
    q.popleft()
    try:
        q.append(clist[i+k])
    except:
        break
print(ans)