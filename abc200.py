n = int(input())
alist = list(map(int,input().split()))

def dp(n):
    if n == 1:
        return 0
    else:
        add = 0
        for i in range(n-1):
            if (alist[i]-alist[n-1])%200==0:
                add += 1
        count = dp(n-1) + add
        return count 

print(dp(n))