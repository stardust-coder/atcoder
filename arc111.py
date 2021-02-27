# import math
# n,m = map(int,input().split())

# def power_func(a,n,p):
#     bi = str(format(n,"b"))#2進表現に
#     res = 1
#     for i in range(len(bi)):
#         res = (res*res) %p
#         if bi[i] == "1":
#             res = (res*a) %p
#     return res

# b = power_func(10,n,m**2)
# res = math.floor(b/m)%m
# print(res)
import copy
import collections

n = int(input())
cardbox = []
values = []
id = []
all = []
for _ in range(n):
    a,b = list(map(int,input().split()))
    #cardbox.append([a,b])
    all.append(a)
    all.append(b)
    if a != b:
        values.append(a)
        values.append(b)
    else:
        id.append(a)

temp = len(set(values))

if n == 1:
    print(1)
else:
    if n <= temp:
        print(n)
    else:
        print(min(len(set(all)),temp+len(set(id))))