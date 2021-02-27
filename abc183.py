# sx,sy,gx,gy = map(int,input().split())
# x = (-sy*(sx-gx)/(sy+gy)) + sx
# print(x)

#C
# import itertools
# n,k = map(int,input().split())
# timelist = []
# for _ in range(n):
#     time = list(map(int,input().split()))
#     timelist.append(time)
# #print(timelist)
#
# l = [i for i in range(1,n)]
# p = itertools.permutations(l)
# count = 0
# for v in p:
#     timesum = 0
#     for i in range(len(v)):
#         if i == 0:
#             timesum += timelist[0][v[i]]
#         else:
#             timesum += timelist[v[i-1]][v[i]]
#
#     timesum += timelist[v[-1]][0]
#     #print(v,timesum)
#     if timesum == k:
#         count += 1
# print(count)

#D
# N,W = map(int,input().split())
# planlist = []
# tmax = 0
# smin = 0
# for _ in range(N):
#     plan = list(map(int,input().split()))
#     planlist.append(plan)
#     if plan[1] > tmax:
#         tmax = plan[1]
#     if plan[1] < smin:
#         smin = plan[1]
# planlist_new = sorted(planlist,key=lambda x:x[1],reverse=True)
# #print(planlist_new,tmax,smin)

# res = True
# for t in range(smin,tmax):
#     usage = 0
#     for plan in planlist_new:
#         #print(t, plan)
#         if plan[0] <= t < plan[1]:
#             usage += plan[2]
#             if usage > W:
#                 res = False
#                 break
#         elif t >= plan[1]:
#             break
#
# if res == True:
#     print("Yes")
# else:
#     print("No")

# #D
# N,W = map(int,input().split())
# planlist = []
# tmax = 0
# smin = 0
# for _ in range(N):
#     plan = list(map(int,input().split()))
#     planlist.append(plan)
#     if plan[1] > tmax:
#         tmax = plan[1]
#     if plan[1] < smin:
#         smin = plan[1]
# planlist_new = sorted(planlist,key=lambda x:x[0])
#
# time = smin
# res = True
# while time < tmax:
#     sum = 0
#     index = 0
#     if planlist_new[-1][0] <= time:
#         index = N
#     else:
#         while planlist_new[index][0] <= time:
#             index += 1
#     #print(index)
#     for plan in planlist_new[:index+1]:
#         print(plan)
#         if plan[0] <= time < plan[1]:
#             sum += plan[2]
#
#         if sum > W:
#             res = False
#             break
#     time += 1
#
# if res == True:
#     print("Yes")
# else:
#     print("No")

#F
# n,q = map(int,input().split())
#
# teams = []
# for i in range(n):
#     teams.append(i)
# classes = list(map(int,input().split()))
# print(teams,classes)
# groupnum = n
# def query1(a,b,teams,num):
#     tempa = teams[a-1]
#     tempb = teams[b-1]
#     for i in range(n):
#         if teams[i] == tempa or teams[i] == tempb:
#             teams[i] = num
#
# def query2(x,y,teams,classes):
#     team = teams[x-1]
#     count = 0
#     for i in range(n):
#         if teams[i] == team and classes[i]==y:
#             count += 1
#     #print(count)
#
# for _ in range(q):
#     c,a,b = map(int,input().split())
#     if c == 1:
#         query1(a,b,teams,groupnum)
#         groupnum += 1
#
#     if c == 2:
#         query2(a,b,teams,classes)
# #D
# N,W = map(int,input().split())
# planlist = []
# tmax = 200000
# smin = 0
# ls = [0]*tmax
# for _ in range(N):
#     plan = list(map(int,input().split()))
#     # planlist.append(plan)
#     # if plan[1] > tmax:
#     #     tmax = plan[1]
#     # if plan[1] < smin:
#     #     smin = plan[1]
#     ls[plan[0]:plan[1]] = [plan[2]]*(plan[1]-plan[0]+1)
#
# if max(ls)<W:
#     print("No")
# else:
#     print('Yes')
