# import math
# n = int(input())
# li = sorted(list(map(int,input().split())), reverse = True)
#
# if 0 in li:
#     print(0)
# else:
#     ans = 1
#     limit = 10**18
#     for i in range(n):
#         if li[i] > limit:
#             ans = -1
#             break
#         else:
#             ans = ans * li[i]
#             limit = limit/li[i]
#     if ans > 10**18:
#         ans = -1
#     print(ans)
from decimal import Decimal
a, b = map(str,input().split())
c = Decimal(a)
d = Decimal(b)
e = c * d
print(e)


# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])
#
#     if temp!=1:
#         arr.append([temp, 1])
#
#     if arr==[]:
#         arr.append([n, 1])
#
#     return arr
#
# n = int(input())
# if n == 1:
#     print(0)
# else:
#     answer = 0
#     for factor in factorization(n):
#         x = factor[1]
#         kouho = int((2*x)**0.5)-1
#         if (kouho)*(kouho+1)/2 <=x and x < (kouho+1)*(kouho+2)/2:
#             kaisu = kouho
#         else:
#             kaisu = kouho+1
#         answer += kaisu
#
#     print(answer)

#e
# n = int(input())
# alist = []
# blist = []
# for i in range(n):
#     a,b = map(int,input().split())
#     alist.append(a)
#     blist.append(b)
#
# N = len(alist)
# alist.sort()
# blist.sort()
# # 偶数の場合
# if N % 2 == 0:
#     median1 = N/2
#     median2 = N/2 + 1
#     median1 = int(median1) - 1
#     median2 = int(median2) - 1
#     amedian = (alist[median1] + alist[median2]) / 2
#     bmedian = (blist[median1] + blist[median2]) / 2
#     ans = (bmedian-amedian)*2+1
# # 奇数の場合
# else:
#     median = (N + 1) / 2
#     median = int(median) - 1
#     amedian = alist[median]
#     bmedian = blist[median]
#     ans = bmedian-amedian+1
# print(int(ans))

#f
# n, s = map(int,input().split())
# integer_list=[input() for i in range(n)]
