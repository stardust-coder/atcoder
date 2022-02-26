# #D
# n,q = map(int,input().split())
# g = [[] for _ in range(n)]
# score = [0 for _ in range(n)]
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     g[a-1].append(b-1)
#     g[b-1].append(a-1)

# from collections import deque

# def bfs(u):
#     queue = deque([u])
#     d = [None] * n # uからの距離の初期化
#     d[u] = 0 # 自分との距離は0
#     while queue:
#         v = queue.popleft()
#         for i in g[v]:
#             if d[i] is None:
#                 d[i] = d[v] + 1
#                 queue.append(i)
#     return d

# # 0からの各頂点の距離
# distance = bfs(0)

# for _ in range(q):
#     c,d = map(int,input().split())
#     if (distance[c-1]+distance[d-1])%2 == 0:
#         print("Town")
#     else:
#         print("Road") 

#E

global heiro
heiro = False

def dfs(L, colors, v):
    colors[v] = 'grey'
    for nv in L[v]:
        if colors[nv] == "grey":
            print("hoge")
            heiro = True
            break
        elif colors[nv] == 'white':
            dfs(L, colors, nv)
    colors[v] = 'black'



n = int(input())
tdict = []
head = []
tail = []
for _ in range(n):
    s = input()
    tdict.append(s)
    head.append(s[:3])
    tail.append(s[-3:])
#print(tdict)

nextdict = [[] for _ in range(n)]
#nextdictづくり
#ココガデキナカッタ
nextdict = [[],[],[],[2,4],[]]

#閉路検出
heiro = False
for i in range(len(head)):
    if head[i] == tail[i]:
        heiro = True

def judge(people,word):
    kouho = nextdict[word]
    if kouho == []:
        return people
    else:
        res = people
        for k in kouho:
            if judge((people+1)%2, k) == (people+1)%2:
                res = (people+1)%2
        return res


for s in range(n):
    if heiro == True:
        print("Draw")
    else:
        j = judge(0,s)
        if j == 0:
            print("Takahashi")
        else:
            print("Aoki")
