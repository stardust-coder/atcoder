n = int(input())

g = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n-1):
    u,v,w = map(int,input().split())
    
    for i in range(n):
        a = max(g[u-1])
        b = max(g[v-1])
        g[max(u,v)-1][i] = max(a,b)    
    g[max(u,v)-1][min(u,v)-1] = w
    
print(g)