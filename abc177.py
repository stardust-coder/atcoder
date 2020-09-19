# n = int(input())
# int_list = list(map(int,input().split()))
#
# e = 1000000007
# X = sum([i for i in int_list])
# square_sum = sum([i**2 for i in int_list])%e
# square = (X**2)%e
# ans = int((square-square_sum))
# ans = int(ans%e)
# print(int(ans/2))
n = int(input())
intlist = list(map(int,input().split()))
mod = 1000000007

sum = 0
for i in range(n):
  sum += intlist[i]
  sum %= mod

ans = sum*sum%mod

for i in range(n):
  ans -= intlist[i]*intlist[i]%mod
  if ans < 0:
    ans += mod

ans *= (mod+1)/2
ans %= mod
print(int(ans))




# import collections
# n,m = map(int,input().split())
#
# indexlist = [0 for i in range(n)]
# indexnum = 1
# for _ in range(m):
#     a,b = map(int,input().split())
#     x = indexlist[a-1]
#     y = indexlist[b-1]
#     if x == 0 and y == 0:
#         indexlist[a-1] = indexnum
#         indexlist[b-1] = indexnum
#         indexnum += 1
#     elif x == 0 and y != 0:
#         indexlist[a-1] = y
#     elif x != 0 and y == 0:
#         indexlist[b-1] = x
#
# indexlist_new = [i for i in indexlist if i > 0]
# c = collections.Counter(indexlist_new)
#
# often = c.most_common()[0][1]
# print(often)

#import math
# from functools import reduce
#
# a = "pairwise coprime"
# b = "setwise coprime"
# c = "not coprime"
# n = int(input())
# int_list = list(map(int,input().split()))
# int_list.sort()
#
# def lcm_base(x, y):
#     return (x * y) // math.gcd(x, y)
# def lcm_list(numbers):
#     return reduce(lcm_base, numbers, 1)
# #print(lcm_list(int_list))
#
# lcm = lcm_list(int_list)
# multi = reduce(lambda x,y:x*y,int_list)
#
# ans = int_list[0]
# for i in range(1, n):
#     ans = math.gcd(ans, int_list[i])
#
# if lcm == multi:
#     print(a)
# elif ans == 1:
#     print(b)
# else:
#     print(c)
