# n, k = map(int,input().split())
# data = []
# for _ in range(k):
#     d = int(input())
#     data.extend(list(map(int,input().split())))
#
# print(n-len(set(data)))

#3
# n,m = map(int,input().split())
# heightlist = list(map(int,input().split()))
# #heightlistの[i]がi-1の展望台の高さ
# rinsetulist = []
# for _ in range(n):
#     rinsetulist.append([])
#
# for _ in range(m):
#     a,b = map(int,input().split())
#     rinsetulist[a-1].append(heightlist[b-1])
#     rinsetulist[b-1].append(heightlist[a-1])
# #print(rinsetulist)
#
# count = 0
# for i in range(n):
#     if rinsetulist[i] == []:
#         count += 1
#     elif heightlist[i] > max(rinsetulist[i]):
#         count += 1
#
# print(count)

#4
# x = int(input())
#
# def make_divisors(n):
#     divisors = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n//i)
#
#     #divisors.sort()
#     return divisors
#
# kouho = make_divisors(x)
#
# #A>0,B<0
# for y in kouho:
#     for a in range(1000):
#         b = a-y
#         if a**5 - b**5 == x:
#             print(a,b)
#             break

#5
# n = int(input())
# height = list(map(int,input().split()))
#
# def numberofpairs(k):#1からkまでの中のペア数を返す
#     if k==2:
#         return 0
#     else:
#         newpair = 0
#         if height[k-1] < k:
#             for x in range(1,k):
#                 if height[k-1] + height[k-x-1] == x:
#                     #print(height[k-1],height[k-x-1],k,x)
#                     newpair += 1
#         num = numberofpairs(k-1) + newpair
#         return num
#
# print(numberofpairs(n))

#5revenge
n = int(input())
height = list(map(int,input().split()))
y = min(height)
listi = []
listj = []
count = 0
for x in range(1+y,n-y+1):#とりうる
    counti = 0
    countj = 0
    for i in range(n):
        if i+1+height[i] == x:
            #print(i,height[i],x)
            #listi.append(x)
            counti += 1
        if i+1-height[i] == x:
            #print(i,height[i],x)
            #listj.append(x)
            countj += 1
    count += counti * countj
    #print(count,counti,countj)

print(count)
