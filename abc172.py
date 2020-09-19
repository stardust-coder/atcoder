# n,m,k = map(int,input().split())
# deskA = list(map(int,input().split()))
# deskB = list(map(int,input().split()))
# bookcount = 0
# time = 0
#
# A = [0]
# B = [0]
# for i in range(len(deskA)):
#     A.append(A[-1]+deskA[i])
#     B.append(B[-1]+deskB[i])
#
# ls = []
# max = 0
# for j in range(len(A)):
#     for l in range(len(B)):
#         remain = k - max

n,m,k = map(int,input().split())
deskA = list(map(int,input().split()))
deskB = list(map(int,input().split()))
bookcount = 0
time = 0
a = 0
b = 0
while time <= k:
    if a == len(deskA) and b == len(deskB):
        bookcount += 1
        break
    elif b == len(deskB):
        t = deskA[a]
        a += 1
    elif a == len(deskA):
        t = deskB[b]
        b += 1
    elif deskA[a] < deskB[b]:
        t = deskA[a]
        a += 1
    elif deskA[a] > deskB[b]:
        t = deskB[b]
        b += 1
    else:
        if deskA[a:] < deskB[b:]:
            t = deskA[a]
            a += 1
        else:
            t = deskB[b]
            b += 1
    time += t
    bookcount += 1

print(bookcount-1)








# import collections
# n = int(input())
#
# def prime_factorize(n):
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a
#
# sum = 0
# for j in range(1,n+1):
#     c = collections.Counter(prime_factorize(j))
#     clist = list(c.values())
#     kosu = 1
#     for i in range(len(clist)):
#         kosu *= clist[i]+1
#     sum += j*kosu
# print(sum)
