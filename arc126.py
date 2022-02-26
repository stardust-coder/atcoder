# t = int(input())

# # 4-4-2
# # 4-3-3
# # 4-2-2-2
# # 3-3-2-2
# # 2-2-2-2-2

# def onlytwofour(t,f):
#     fft = min(int(f/2),t)
#     f -= fft*2
#     t -= fft
#     ttttt = int(t/5)
#     return fft+ttttt


# def sousa(a,b,c):
#     temp = a+c*2
#     thth = min(int(b/2),int(temp/2))
#     temp -= 2*thth
#     b -= 2*thth
#     if b == 0:
#         if temp > a:
#             return thth+onlytwofour(a,int((temp-a)/2))
#         else:
#             return thth+onlytwofour(temp,0)
#     else:
#         return thth


# ans = []
# for _ in range(t):
#     n2,n3,n4 = map(int,input().split())
#     temp = sousa(n2,n3,n4)
#     ans.append(temp)
# for item in ans:
#     print(item)

# Hopcroft-Karp Algorithm
from collections import deque
class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2+N0+N1
        self.G = [[] for i in range(N)]
        for i in range(N0):
            forward = [2+i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.G[0].append(forward)
            self.G[2+i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2+N0+i, 0, forward]
            bs.append(backward)
            self.G[2+N0+i].append(forward)
            self.G[1].append(backward)

    def add_edge(self, fr, to):
        #assert 0 <= fr < self.N0
        #assert 0 <= to < self.N1
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.G[v0].append(forward)
        self.G[v1].append(backward)

    def bfs(self):
        G = self.G
        level = [None]*self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] is not None

    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0

    def flow(self):
        flow = 0
        G = self.G
        bfs = self.bfs; dfs = self.dfs
        while bfs():
            *self.it, = map(iter, G)
            while dfs(0, 1):
                flow += 1
        return flow

    def matching(self):
        return [cap for _, cap, _ in self.backwards]

n,m = map(int,input().split())
c = HopcroftKarp(n,n)
for _ in range(m):
    a,b = map(int,input().split())
    c.add_edge(a-1,b-1)
c.flow()
res = c.matching()
print(res)