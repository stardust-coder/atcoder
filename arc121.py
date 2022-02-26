# n = int(input())
# houses = []
# for i in range(n):
#     houses.append(list(map(int,input().split()))+[i])
# ##print(houses)

# xsort = sorted(houses, key=lambda x:x[0],reverse=True)
# #print(xsort)
# ysort = sorted(houses, key=lambda x:x[1],reverse=True)
# #print(ysort)
# x1 = xsort[0][0]-xsort[-1][0]
# x2 = xsort[0][0]-xsort[-2][0]
# x3 = xsort[1][0]-xsort[-1][0]
# #print(x1,x2,x3)
# y1 = ysort[0][1]-ysort[-1][1]
# y2 = ysort[0][1]-ysort[-2][1]
# y3 = ysort[1][1]-ysort[-1][1]
# ##print(y1,y2,y3)

# res = sorted([x1,x2,x3,y1,y2,y3],reverse=True)

# if {res[0],res[1]} == {x1,y1} and {xsort[0][-1],xsort[-1][-1]} == {ysort[0][-1],ysort[-1][-1]}:
#     print(res[2])
# else:
#     print(res[1])

#B
# n = int(input())
# r = []
# g = []
# b = []

# def closest(l1,l2):
#     if l1 == [] or l2 == []:
#         return 1e15
#     else:
#         l1.sort()
#         l2.sort()
#         i = 0
#         j = 0
#         kouho = abs(l1[i]-l2[j])
#         while True:
#             #print(i,j)
#             if l1[i] > l2[j]:
#                 j += 1
#                 if j == len(l2):
#                     break
#                 temp = abs(l1[i]-l2[j])
#                 if kouho > temp:
#                     kouho = temp
#             else:
#                 i += 1
#                 if i == len(l1):
#                     break
#                 temp = abs(l1[i]-l2[j])
#                 if kouho > temp:
#                     kouho = temp
#         return kouho
# #print("c",closest([10,2,3],[1,4,5]))


# for _ in range(2*n):
#     a,c = input().split()
#     if c == "R":
#         r.append(int(a))
#     elif c == "G":
#         g.append(int(a))
#     else:
#         b.append(int(a))
# #print(r,g,b)
# if (len(r)%2 == 0 and len(g)%2 == 0) and len(b)%2 == 0:
#     print(0)
# elif len(r)%2==0:
#     print(min(closest(g,b),closest(g,r)+closest(b,r)))
# elif len(g)%2==0:
#     print(min(closest(r,b),closest(r,g)+closest(b,g)))
# else:
#     print(min(closest(r,g),closest(g,b)+closest(r,b)))

#D 1or2

n = int(input())
ame = list(map(int,input().split()))
ame.sort()

def calc(l):#all pos
    l.sort()
    res = min(abs(l[-1]-l[0]),abs(l[-1]-l[0]-l[1]),abs(l[-1]+l[-2]-l[0]-l[1]))
    return res


neg = [a for a in ame if a < 0]
pos = [a for a in ame if a >= 0]
pos.sort(reverse=True)
ls = []
if len(neg) < len(pos):
    for k in range(len(neg)):
        #pos[k] += neg[k]
        ls.append(neg[k]+pos[k])
    remain = pos[len(neg):]
    
else:
    for k in range(len(pos)):
        #neg[k] += pos[k]   
        ls.append(neg[k]+pos[k])  
    remain = neg[len(pos):]

m2 = calc(remain)
if ls == []:
    print(m2)
else:
    mx1 = max(ls)
    mn1 = min(ls)
    print(min(mx1-mn1,m2))
#ls = pos
#print(max(ls) - min(ls))

