# n = int(input())
# import numpy as np
# s = np.zeros((n,n))
# t = np.zeros((n,n))

# for i in range(n):
#     sl = input()
#     for j in range(len(sl)):
#         if sl[j] == "#":
#             s[i][j] = 1

# for i in range(n):
#     tl = input()
#     for j in range(len(tl)):
#          if tl[j] == "#":
#             t[i][j] = 1

# res = False

# s1 = s
# s2 = np.rot90(s1)
# s3 = np.rot90(s2)
# s4 = np.rot90(s3)

# for mat in [s1,s2,s3,s4]:
#     for a in range(n):
#         for b in range(n):
#             tprime = np.roll(np.roll(mat,a,axis=0),b,axis=1)
#             if np.allclose(tprime, t):
#                 res = True
#                 break

# if res == True:
#     print("Yes")
# else:
#     print("No")           

#C...AC
# scor = []
# n = int(input())
# for i in range(n):
#     s = input()
#     for j in range(n):
#         if s[j]=="#":
#             scor.append((i,j))

# tcor = []
# tlist = []
# for i in range(n):
#     t = input()
#     tlist.append(t)

# for k in range(len(tlist)):
#     for j in range(n):
#         if tlist[k][j] == "#":
#             tcor.append((k,j))


# if len(scor)!=len(tcor):
#     print("No")
# else:
#     res = False
#     s1 = scor
#     s2 = [(x[1],-x[0]) for x in scor]
#     s3 = [(-x[0],-x[1]) for x in scor]
#     s4 = [(-x[1],x[0]) for x in scor]
    
#     for sprime in [s1,s2,s3,s4]:
#         sprime.sort()
#         d1 = sprime[0][0]-tcor[0][0]
#         d2 = sprime[0][1]-tcor[0][1]
#         tnew = [(a[0]+d1,a[1]+d2) for a in tcor]
        
#         if sprime == tnew:
#             res = True
#             break
#     #print(res)
#     if res == True:
#         print("Yes")
#     else:
#         print("No")

# #D
# n = int(input())
# cor = []
# for _ in range(n):
#     x,y = map(int,input().split())
#     cor.append((x,y))
# #print(cor)


# cor.sort()
# s = set(cor)

# count = 0
# import itertools
# patterns = list(itertools.combinations(range(n),2))
# for p in patterns:
#     cor1 = cor[p[0]]
#     cor2 = cor[p[1]]
#     if cor1[0]!=cor2[0] and cor1[1]!=cor2[1]:
#         new1 = (cor1[0],cor2[1])
#         new2 = (cor2[0],cor1[1])
#         if new1 in s and new2 in s:
#             #print(cor1,cor2,new1,new2)
#             count += 1
#     else:
#         pass

# print(int(count/2))

#E
n,m = map(int,input().split())
import heapq

next = [[] for _ in range(n+1)]   # 隣接管理のリスト
total = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    total += c
    next[a-1].append((c, b-1))
visited = [0] * n
connection = 0
q = [(0, 0)]    # (cost, v)
heapq.heapify(q)
ans = 0
while len(q):
    cost, v = heapq.heappop(q)
    if visited[v]:
        continue

    # そのノードと繋げる
    visited[v] = 1
    connection += 1
    ans += cost

    # 新たに繋げたノードから行けるところをエンキュー
    for i in next[v]:
        heapq.heappush(q, i)

    # 全部のノードが繋がったら終了
    if connection == n:
        break

print(total,ans)
print(total-ans)

