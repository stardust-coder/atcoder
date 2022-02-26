# n = int(input())
# s = input()#長さ2N
# q = int(input())

# s1 = [s[i] for i in range(n)]
# s2 = [s[i] for i in range(n,2*n)]
# order = True

# def t1(s1,s2,order,a,b):
#     #print(s1,s2,order,a,b)
#     if order == True:
#         if a <= n and b <= n:
#             s1[a-1],s1[b-1] = s1[b-1],s1[a-1] 
#         elif a <= n and b >= n+1:
#             s1[a-1],s2[b-n-1] = s2[b-n-1],s1[a-1] 
#         else:
#             s2[a-n-1],s2[b-n-1] = s2[b-n-1],s2[a-n-1] 
#         return s1,s2, True
#     else:
#         if a <= n and b <= n:
#             s2[a-1],s2[b-1] = s2[b-1],s2[a-1] 
#         elif a <= n and b >= n+1:
#             s2[a-1],s1[b-n-1] = s1[b-n-1],s2[a-1] 
#         else:
#             s1[a-n-1],s1[b-n-1] = s1[b-n-1],s1[a-n-1] 
#         return s1,s2, False

# def t2(order):
#     if order == True:   
#         return False
#     else:
#         return True


# for _ in range(q):
#     t,a,b = map(int,input().split())
#     if t == 1:
#         s1,s2,order = t1(s1,s2,order,a,b)
#     else:
#         order= t2(order)
#     #print(s1,s2,order)

# if order == True:
#     print("".join(s1) + "".join(s2))
# else:
#     print("".join(s2) + "".join(s1))

#D
n,m = map(int,input().split())
color = [None for _ in range(n+1)]
G = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
#print(color)

count = 0
def dfs(v,c):
    global count
    
    #print(v,c)
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]]==c:
            return False
        if color[G[v][i]]==None:
            if c == 1:
                dfs(G[v][i],0)
                dfs(G[v][i],-1)
            elif c == 0:
                dfs(G[v][i],1)
                dfs(G[v][i],-1)
            elif c == -1:
                dfs(G[v][i],1)
                dfs(G[v][i],0)
            return False
    count += 1
    print("色",color)
    print("count",count)
    return 

for start in range(1,n+1):
    for cstart in [-1,0,1]:
        print(start,cstart)
        dfs(start,cstart)
print(count)