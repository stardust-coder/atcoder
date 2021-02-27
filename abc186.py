# h,w = map(int,input().split())
# a = []
# for _ in range(h):
#     ls = list(map(int,input().split()))
#     a.extend(ls)
#
# goukei = sum(a)
# mini = min(a)
# ans = int(goukei - mini*len(a))
# print(ans)

#C
# N = int(input())
# count = 0
# for i in range(1,N+1):
#     st = list(str(i))
#     hachi = list(str(oct(i)))
#     if "7" not in st and "7" not in hachi:
#         count += 1
# print(count)

#D
# n = int(input())
# a = sorted(list(map(int,input().split())))
#
# res = a[1]-a[0]
# sum = a[1]+a[0]
# for i in range(2,len(a)):
#     item = a[i]
#     res += a[i]*i-sum
#     sum += item
# print(res)

#E
# import math
# T = int(input())
# for t in range(T):
#     n,s,k = map(int,input().split())
#     if k > n:
#         k = k%n
#     remainder = n-s
#     if remainder%k==0:
#         print(int(remainder/k))
#     else:
#         key = math.gcd(n,k)
#         if key == 1:
#             print("-1")
#         else:
#             ichi = s
#             count = 0
#             while True:
#                 ichi += k
#                 count += 1
#                 ichi = ichi%n
#                 if ichi == 0:
#                     print(count)
#                     break
#                 if ichi == s:
#                     print("-1")
#                     break
# import math
# T = int(input())
# for t in range(T):
#     n,s,k = map(int,input().split())
#     if k > n:
#         k = k%n
#     ans = -1
#     for i in range(1,100000):
#         if (i*n-s)/k >= 1 and (i*n-s)%k==0:
#             ans = int((i*n-s)/k)
#             break
#     print(ans)

#こたえ：modinvをつかえばよい
# -s == zk(modN)ととけば良い
#z = kinv*(-s) modN

def extgcd(a,b):
    d = a
    if b != 0:
        d,y,x = extgcd(b,a%b)
        y -= (a/b)*x
    else:
        x = 1.
        y = 0.
    return d,x,y

def modinv(a,m):
    extgcd(a,m,x,y)
    return (m+x%m)%m
    
print(extgcd(4,11))
