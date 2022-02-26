n,m = map(int,input().split())
alist = list(map(int,input().split()))

def mex(ls):
    s = set(ls)
    #print(s)
    num = 0
    print(ls)
    if len(ls) == 1:
        if ls[0] == 0:
            num = 1
        else:
            num = 0
    elif ls[int((len(ls)-1)/2)] <= (len(ls)-1)/2:
        num = mex(ls[:int(len(ls)/2)])
    else:
        num = mex(ls[int(len(ls)/2):])
    return num

def dp(i):
    if i == 0:
        return mex(alist[:m])
    else:
        new = mex(alist[i:i+m])      
        return min(dp(i-1),new)
print(mex([0,1]))
#print(dp(n-m))