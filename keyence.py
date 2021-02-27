# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c = []


# maxa = 0
# maxb = 0
# maxab = 0
# for i in range(n):
#     newa = a[i]
#     newb = b[i]
#     temp = max(maxa*newb, newa*newb, maxab)
#     c.append(temp)
#     if maxa < newa:
#         maxa = newa
#     if maxab < temp:
#         maxab = temp

# for j in c:
#     print(j)

# import collections
# n,k = map(int,input().split())
# balls = list(map(int,input().split()))

# c = collections.Counter(balls)
# ls = sorted(c.items())

# ans = 0
# add = k
# count = 0
# for p in ls:
#     if p[0] != count:
#         break
#     if p[1] >= add:
#         ans += add
#     elif p[1] < add:
#         add = p[1]
#         ans += add
#     count += 1
# print(ans)

# C(500)
H,W,K = map(int,input().split())
##################
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 998244353 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
#################
total = cmb(H+W,W,mod)#そもそもの総数
ls = []
for _ in range(k):
    ls.append(list(map(int,input().split())))

def dp(i,j):
    mod = 998244353 #出力の制限
    if i==1 and j==1:
        if r:
            return [1,0,0,9,1]
        elif d:
            return [0,1,0,9,1]
        elif x:
            return [0,0,1,9,1]
        else:
            return [1,1,1,9,0]
    elif i == 0:
        return [0,0,0,0,0]
    elif j == 0:
        return [0,0,0,0,0]
    else:
        r1 = dp(i-1,j)[0]
        d1 = dp(i-1,j)[1]
        x1 = dp(i-1,j)[2]
        r2 = dp(i,j-1)[0]
        d2 = dp(i,j-1)[1]
        x2 = dp(i,j-1)[2]
        rd = dp(i-1,j)[4]+dp(i,j-1)[4]-dp(i-1,j-1)[4]
        masume = i*j-i-j+1
        three_one = 
        res = (r1+x1)*three_one + (d2+x2)*three_two
        if r:
            r = res
            d = 0
            x = 0
        elif d:
            r = 0
            d = res
            x = 0
        elif x:
            r = 0
            d = 0
            x = res
        else:
            r = res
            d = res
            x = res
        san = dp(i,j)[3]*3%mod  
        return [r,d,x,san,rd]
