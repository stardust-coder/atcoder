# n.m = map(int,input().split())
# jlist = []

# for _ in range(m):
#     a,b = map(int,input().split())
#     jlist.append([a,b])

# k = int(input())

# for i in range(k):
#     c,d = map(int,input().split())

# #D
# import math
# n = int(input())
# count = 0

# def make_divisors(n):
#     divisors = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n//i)

#     divisors.sort()
#     return divisors

# ls = make_divisors(2*n)

# for c in ls:
#     b = c-1
#     a = ((2*n/(b+1))-b)/2
#     ainf = math.floor(a)
#     asup = math.ceil(a)
#     if (ainf*2+b)*(b+1) == 2*n or (asup*2+b)*(b+1) == 2*n:
#         count += 1

# print(count)


#E

n,m = map(int,input().split())
pairls = []
G = [[0]* n for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1
k = int(input())
c = list(map(int,input().split()))
#print("G",G)

import numpy as np
from scipy.sparse.csgraph import shortest_path,connected_components
from scipy.sparse import csr_matrix
a = np.array(G)
# n, labels = connected_components(a)
# #print(n)
# #print(labels)
# res = True
# temp = labels[c[0]-1]
# for stone in c:
#     if labels[stone-1] != temp:
#         res = -1
#         break

# if res == True:

cost = shortest_path(a)
print(cost)
length = 0
for i in range(len(c)-1):
    next = 1 + cost[c[next]-1].index(min(cost[c[i]-1]))
    length += cost[c[i]-1][c[next]-1]
    kouho.append(length)
print(min(min(kouho),-1))
