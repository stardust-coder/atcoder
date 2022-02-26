m = int(input())
adjlist = [[] for _ in range(10)]
for _ in range(m):
    u,v = map(int,input().split())
    adjlist[u].append(v)
    adjlist[v].append(u)

initial = list(map(int,input().split()))

location = [0 for _ in range(9)]
for item in initial:
    location[item-1] = initial.index(item)+1


def dp(l):
    if l==[1,2,3,4,5,6,7,8,0]:
        return 0
    else:
        empty = l.index(0)+1
        kouho = []
        print(empty)
        for node in adjlist[empty-1]:
            l[node],l[empty-1] = 0, l[node]
            kouho.append(dp(l))

        if len(kouho) == 0:
            return 1e10
        else:
            return min(kouho)

print(dp(location))