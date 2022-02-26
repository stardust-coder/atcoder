# n = int(input())
# x,y = map(int,input().split())
# l = []
# for _ in range(n):
#     a,b = map(int,input().split())
#     l.append([a,b])


# alist = sorted(l,key=lambda x: (x[0], x[1]))
# alist.reverse()

# blist = sorted(l,key=lambda x: (x[1], x[0]))
# blist.reverse()


# # clist = sorted(l,key=lambda x: (x[1]+x[0]))
# # clist.reverse()
# # print(clist)

# def sousa(alist,i):
#     count = 0
#     atemp = 0
#     btemp = 0
#     while atemp < x:
#         if count == n:
#             count = -1
#             break
#         atemp += alist[count][0]
#         btemp += alist[count][1]
#         count += 1

#     if count != -1:
#         if btemp >= y:
#             ans = count
            
#         else:
#             remainder = l[count:]
#             remainder.sort(key=lambda x: x[i], reverse=True)
#             bcount = 0
#             while btemp < y:
#                 if bcount == len(remainder):
#                     bcount = -1
#                     break
#                 atemp += remainder[bcount][0]
#                 btemp += remainder[bcount][1]
#                 bcount += 1
#             if bcount == -1:
#                 ans = -1
#             else:
#                 ans = count + bcount

#         return ans
#     else:
#         return -1

# k1 = sousa(alist,1)
# k2 = sousa(blist,0)
# #k3 = sousa(clist)

# if k1==-1 and k2==-1:
#     print(-1)
# elif k1==-1:
#     print(k2)
# elif k2==-1:
#     print(k1)
# else:
#     print(min(k1,k2))
# #print(k3)

n = int(input())
x,y = map(int,input().split())
l = []
for _ in range(n):
    a,b = map(int,input().split())

atemp = 0
btemp = 0
count = 0
while atemp < x or btemp < y:
    l.sort(key=lambda x: (x[0],x[1]))
    atemp += l[-1][0]
    btemp += l[-1][1]
    l.pop(-1)
    count += 1
    if atemp >= x and btemp >= y:
        break
    l.sort(key=lambda x: (x[1],x[0]))
    atemp += l[-1][0]
    btemp += l[-1][1]
    l.pop(-1)
    count += 1
    if atemp >= x and btemp >= y:
        break

print(count)

