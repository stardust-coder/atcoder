import math
n, x, y, z = map(int,input().split())

def comb(n, r):
    if n < r:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

sum = 1
for len in range(4,n+1):
    patternlist = []
    for i in range(1,len+1):
        for j in range(1,len-i):
            patternlist.append([i,j,len-i-j])
    #print(patternlist)
    newnum = 0
    for pattern in patternlist:
        a = pattern[0]
        b = pattern[1]
        c = pattern[2]
        #print(a,b,c)
        newnum += comb(x-1,a-1)*comb(y-1,b-1)*comb(z-1,c-1)
        #print(newnum)
    sum = sum*20+newnum%(10**9+7)

print(sum)
