# import itertools
# import math
#
# n = int(input())
# point_list = []
# for i in range(n):
#     point = list(map(int,input().split()))
#     point_list.append(point)
#
# patterns  = list(itertools.combinations(point_list,3))
#
# def dist(point1,point2):
#     return math.sqrt(int((point1[0]-point2[0])**2+(point1[1]-point2[1])**2))
#
# print(patterns)
# for pattern in patterns:
#     x1 = dist(pattern[0],pattern[1])
#     x2 = dist(pattern[1],pattern[2])
#     x3 = dist(pattern[2],pattern[0])
#     case = "No"
#     print(type(x1))
#     if x1 + x2 == x3 or x1 + x3 == x2 or x2 + x3 == x1:
#         case = "Yes"
#         break
# print(case)

#D
# from collections import Counter
# kouho_ls =  [8* i for i in range(13,126) if 8*i%10 != 0]
# s = int(input())
#
# if s in [8,16,24,32,48,56,64,72,88,96,61,42,23,84,65,46,27,69]:
#     print("Yes")
# else:
#     s = str(s)
#     slist = list(map(int, s))
#     d = Counter(slist)
#     ans = "No"
#     for kouho in kouho_ls:
#         text = list(map(int,str(kouho)))
#         kouhod = list(Counter(text).items())
#         check = []
#         for i in kouhod:
#             a = i[0]
#             b = i[1]
#             check.append(d[a]>=b)
#         if False not in check:
#             ans = "Yes"
#             break
#     print(ans)

n,m = map(int,input().split())
height_ls = list(map(int,input().split()))#n人
w_ls = list(map(int,input().split()))#m種類
w_ls.sort()
height_ls.append(w_ls[0])
min = 1e11
for i in range(m-1):
    height_ls.remove(w_ls[i])
    height_ls.append(w_ls[i+1])
    height_ls.sort()
    ind = height_ls.index(w_ls[i])
    if ind == 0:
        small = 1e11
    else:
        small = w_ls[i] - height_ls[ind-1]
    if ind == n:
        big = 1e11
    else:
        big = height_ls[ind+1] - w_ls[i]
    if min > small:
        min = small
        k = i
    elif min > big:
        min = big
        k = i

def rinsetu(l):
    sum = 0
    for i in range(int(len(l)/2)):
        sum += l[2*i+1]-l[2*i]
    return sum

height_ls.append(w_ls[i])
height_ls.sort()
res = rinsetu(height_ls)
print(res)
