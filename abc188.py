# n,largec = map(int,input().split())

# cost = 0
# plan = 0

# ls = []
# dayls = []
# atemp = 0
# btemp = 0
# for _ in range(n):
#     a,b,c = map(int,input().split())
#     if atemp != a:
#         ls.append([a,c])
#         dayls.append(a)
#         atemp = a
#     else:
#         index = dayls.index(a)
#         ls[index][1] += c
#     if btemp != b:
#         ls.append([b+1,-c])
#         dayls.append(b+1)
#         btemp = b
#     else:
#         index = dayls.index(b+1)
#         ls[index][1] -= c
# sortedls = sorted(ls)

# for j in range(len(sortedls)-1):
#     day = sortedls[j]
#     plan += day[1]
#     cost += min(largec, plan)*(sortedls[j+1][0]-day[0])

# print(cost)

#E

