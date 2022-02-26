#D
# n,m = map(int,input().split())
# graph = [[] for _ in range(n)]
# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a-1].append(b-1)
#     graph[b-1].append(a-1)

# e = 1000000007

# from heapq import heappush, heappop
# INF = 10 ** 9
# def dijkstra(s, n): # (始点, ノード数)
#     dist = [INF] * n
#     keirosu = [0] * n
#     keirosu[0] = 1
#     hq = [(0, s)] # (distance, node)
#     dist[s] = 0
#     seen = [False] * n # ノードが確定済みかどうか
#     while hq:
#         v = heappop(hq)[1] # ノードを pop する
#         seen[v] = True
#         for to in graph[v]: # ノード v に隣接しているノードに対して
#             if seen[to] == False and dist[v] + 1 < dist[to]:
#                 keirosu[to] = keirosu[v]
#                 dist[to] = dist[v] + 1
#                 heappush(hq, (dist[to], to))
#             elif seen[to] == False and dist[v] + 1 == dist[to]:
#                 keirosu[to] += keirosu[v]%e
#     return dist, keirosu

# res = dijkstra(0,n)
# print(res[1][-1]%e)

#E
n = int(input())
k = int(input())
adj = [[] for _ in range(n**2)]

map = [[0]*(n+2) for _ in range(n+2)]


for i in range(n):
    ss = input()
    for j in range(n):
        letter = ss[j]
        if letter == ".":
            map[i+1][j+1] = 1
print(map)
for row in range(1,n+1):
    for column in range(1,n+1):
        if map[row][column] == 1:
            cur = n*row-(n-column)-1
            if map[row+1][column]==1:
                adj[cur].append(cur+n)
            if map[row-1][column]==1:
                adj[cur].append(cur-n)
            if map[row][column+1]==1:
                adj[cur].append(cur+1)
            if map[row][column-1]==1:
                adj[cur].append(cur-1)
print(adj)
        
import itertools
l = [i for i in range(n**2)]
c_list = list(itertools.combinations(l, k))
print(c_list)

# from operator import mul
# from functools import reduce
# def combinations_count(n, r):
#     r = min(r, n - r)
#     numer = reduce(mul, range(n, n - r, -1), 1)
#     denom = reduce(mul, range(1, r + 1), 1)
#     return numer // denom
# print(combinations_count(64,8))

def dfs():
    return list(_dfs(0))

def _dfs(node):
    if node is leaf:
        yield [node]
    else:
        for child in children of node:
            for path in _dfs(child):
                yield [node] + path

print(dfs())