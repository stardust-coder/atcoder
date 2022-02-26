#D
import copy
n,q = map(int,input().split())
a = list(map(int,input().split()))

qlist = []
for index in range(q):
    k = int(input())
    qlist.append([k,index])
qlist.sort()
#print(qlist)
plist = copy.deepcopy(qlist)

l = []
temp = 0
c = 0
v = 1
for i in range(len(a)):
    dif = a[i]-temp
    if dif != 1:
        l.append([v,c])
        v += dif-1
    c += 1
    temp = a[i]
l.append([v,c])


c = 0
ans = []
for j in range(len(l)):
    c += l[j][0]
    if qlist[0][0] < c:
        ans.append(l[j-1][1])
        qlist.pop(0)

while len(ans)!=len(plist):
    ans.append(l[-1][1])

for z in range(len(plist)):
    plist[z][0] = plist[z][0]+ans[z]

plist.sort(key=lambda x : x[1])

for k in range(len(ans)):
    print(plist[k][0])


   
