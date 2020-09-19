#D TLE
n,k = map(int,input().split())
s = []
for _ in range(k):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        s.append(i)
goal = n-1
flist = [0 for _ in range(n)]#flist[i]でf(i)の値

flist[0] = 1
for current in range(n):
    if flist[current] != 0:
        for num in s:
            if current+num <= n-1:
                flist[current+num] += flist[current]

print(flist[-1]%998244353)

#E
