# a1,a2,a3 = map(int,input().split())
# center = (a1+a3)/2
# import math
# if center >= a2:
#     if (a1+a3)%2==0:
#         print(int(center)-a2)
#     else:
#         print(int(center)-a2+2)

# else:
#     small = min(a1,a3)
#     big = max(a1,a3)
#     goal = 2*a2-small
#     print(goal-big)


# n = int(input())
# alist = list(map(int,input().split()))
# blist = list(map(int,input().split()))
# clist = list(map(int,input().split()))
# all = []
# for a in alist:
#     all.append([a,"a"])
# for b in blist:
#     all.append([b,"b"])
# for c in clist:
#     all.append([c,"c"])
# li = sorted(all)

# from collections import deque
# anum = 0
# abnum = 0
# abcnum = 0
# alast = deque()
# ablast = deque()
# abclast = 0

# count = 0
# now = "a"
# for item in li:
#     if item[1]=="a":
#         anum += 1
#         alast.append(item[0])
#     elif item[1]=="b":
#         if anum!=0:
#             if alast[0] < item[0]:
#                 anum -= 1
#                 abnum += 1
#                 alast.popleft()
#                 ablast.append(item[0])
#     elif item[1] == "c":
#         if abnum != 0:
#             if ablast[0] < item[0]:
#                 abnum -= 1
#                 abcnum += 1
#                 ablast.popleft()

# print(abcnum)



import math
def case(n):
    st = list(map(int, str(n)))

    if set(st) <= {1,2,3} :
        return 1
    
    keta = int(math.log10(n))+1 
    three = int("3"*(keta))
    if n < three:
        three =  int("3"*(keta-1))
    shou = int(n/three)
    amari = n%three
    ans = case(amari)+shou
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    ans = case(n)
    print(ans)