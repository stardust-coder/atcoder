# n,m,t = map(int,input().split())
# charge = n
# last = 0
# res = "Yes"
# for _ in range(m):
#     a,b = map(int,input().split())
#     charge -= a-last
#     #print(charge)
#     if charge <= 0:
#         res = "No"
#         break
#     charge += b-a
#     if charge >= n:
#         charge = n
#     #print(charge)
#     last = b
# #print(t,last)
# charge -= t-last
# if charge <= 0:
#     res = "No"
# print(res)

#C
# import math
# L = int(input())
# def combinations_count(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
#
# print(combinations_count(L-1,11))

#D
# import math
# N,M = map(int,input().split())
# count = 1
# alist = [1]
# als = list(map(int,input().split()))
# alast = [N]
# alist.extend(als)
# alist.extend(alast)
# print(alist)
#
# def gcdzero(a,b):
#     if a<=0 or b <= 0:
#         return 0
#     else:
#         return math.gcd(a,b)
#
#
# if M == 0 or als==[1] or als==[N]:
#     print(1)
# else:
#     hanko = als[1]-als[0]-1
#     for i in range(M+1):
#         haba = alist[i+1]-alist[i]-1
#         if haba > 0:
#             newhanko = gcdzero(hanko,haba)
#             if newhanko!=0:
#                 count *= int(hanko/newhanko)#バイリツ
#                 count += int(haba/newhanko)
#             hanko = newhanko
#             print(count)
#
#     print("res",count)

# import math
# N,M = map(int,input().split())
#
# alist = [0]
# als = sorted(list(map(int,input().split())))
# alast = [N+1]
# alist.extend(als)
# alist.extend(alast)
#
# sa = []
# for i in range(M+1):
#     dif= alist[i+1]-alist[i]-1
#     if dif != 0:
#         sa.append(dif)
# if sa==[]:
#     print(0)
# elif M==0:
#     print(1)
# else:
#     hanko = min(sa)
#     count = 0
#     for length in sa:
#         count += math.ceil(length/hanko)
#     print(count)

#E
N,M = map(int,input().split())
alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

minx = abs(N-M)
