n = int(input())
alist = list(map(int,input().split()))
plus = 1
minus = 1
ans = 2*alist[0]
res = [alist[0],2*alist[0]]
length = [1,2]


dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 2
for i in range(2, n+1):
    dp[i] = (dp[i - 1]%1000000007 + dp[i-2]%1000000007)%1000000007
#print(dp)

for i in range(2,n):
    if i == 2:
        k = 0
        l = 1
    else:
        k =res[i-3]%1000000007
        l = dp[i-3]%1000000007
    #print(i,res,length,alist)
    drop = k%1000000007+(alist[i-2]%1000000007-alist[i-1]%1000000007-alist[i]%1000000007)*l
    #print(ans,drop)
    ans = (ans*2-drop)
    ans = ans%1000000007
    res.append(ans)
    # kei = (plus+minus)*2-minus
    # plus = plus + minus
    # minus = kei-plus
    # length.append(kei)
print(res[n-1])

# n = int(input())
# alist = list(map(int,input().split()))
# alist.sort()
# #print(alist)
# kouho = []
# asum  = 0
# if n == 1:
#     print(alist[0]/2)
# else:
#     for a in range(1,n):
#         asum += alist[a-1]
#         if 2*a >= n:
#             x = alist[a-1]/2
#         else:
#             x = alist[a]/2
#         res = x - ((n-a)*2*x/n) - (asum/n)
#         kouho.append(res)

#     print(sum(alist)/n+min(kouho))

# n = int(input())
# x = 0
# y = 0
# def one(x,y):
#     return x+1,y
# def two(x,y):
#     return x,y+1
# def three(x,y):
#     return x+y,y
# def four(x,y):
#     return x,x+y

# a = 1
# b = 0
# k = 0
# while a < n:
#     k += 1
#     a,b = a+b,a
#     print(a,b)
# print(k)