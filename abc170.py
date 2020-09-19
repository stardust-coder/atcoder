# x,n = map(int,input().split())
# plist = list(map(int,input().split()))
# j=0
# while True:
#     if x-j not in plist:
#         print(x-j)
#         break
#     if x+j not in plist:
#         print(x+j)
#         break
#     j += 1

#D
n = int(input())
alistold = list(map(int,input().split()))
alist = sorted(alistold)

k=0
while k<=len(alist)-1:
    unit = alist[k]
    ls =  [i for i in alist if i%unit!=0]
    alist = [unit] + ls
    k+=1

choufuku = 0
choufukulist = [x for x in set(alistold) if alistold.count(x) > 1]
for num in alist:
    if num in choufukulist:
        choufuku += 1

print(k-choufuku)

#E
# n,q = map(int,input().split())
# childlist = [[] for _ in range(2*(10**5))]
# memberlist = []
# fairnesslist = []
#
# def query(c,d):
#     score = memberlist[c-1][0]#cのレーと
#     before = memberlist[c-1][1]
#     childlist[before-1].remove([c,score])
#     childlist[d-1].append([c,score])
#     maxlist=[]
#     for kindagarten in childlist:
#         if kindagarten != []:
#             saidai = max(kindagarten, key=lambda x:x[1])
#             maxlist.append(saidai[1])
#
#     fairness = min(maxlist)
#     fairnesslist.append(fairness)
#     return
#
# for i in range(n):
#     a,b = map(int,input().split())
#     childlist[b-1].append([i+1,a])
#     memberlist.append([a,b])
#
# for _ in range(q):
#     c,d = map(int,input().split())
#     query(c,d)
#
# for j in range(q):
#     print(fairnesslist[j])
