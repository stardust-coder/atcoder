#D
import math
n = int(input())
slist = []
tlist = []
gs = [0,0]
gt = [0,0]
for _ in range(n):
    a,b = map(int,input().split())
    slist.append([a,b])
    gs[0] += a
    gs[1] += b
for _ in range(n):
    c,d = map(int,input().split())
    tlist.append([c,d])
    gt[0] += c
    gt[1] += d

gs[0] = gs[0]/n
gs[1] = gs[1]/n
gt[0] = gt[0]/n
gt[1] = gt[1]/n

for i in range(n):
    slist[i][0] -= gs[0]
    slist[i][1] -= gs[1]
    tlist[i][0] -= gt[0]
    tlist[i][1] -= gt[1]


# def check(s,t):
#     s.sort()
#     t.sort()
#     res = True
#     for l in range(len(t)):
#         if abs(s[l][0]-t[l][0]) > 1e-10:
#             res = False
#         if abs(s[l][1]-t[l][1]) > 1e-10:
#             res = False
#     return res


# res = False
# for p in [math.pi/2, math.pi, 3*math.pi/2, 2*math.pi]:
#     t = []
#     s = []
#     for k in range(len(tlist)):
#         x = math.floor((tlist[k][0]*math.cos(p)+tlist[k][1]*math.sin(p))*(10**5))/(10**5)
#         y = -tlist[k][0]*math.sin(p)+tlist[k][1]*math.cos(p)
#         s.append([math.floor(slist[k][0]*(10**5))/(10**5),slist[k][1]])
#         t.append([x,y])
#     res = check(s,t)
#     if res == True:
#         break
# print(res)


def near(x):
    return math.floor(x*(10**8))/(10**8)



def chousei(x):
    if x < 0:
        return near(x + 2*math.pi)
    elif x > 2*math.pi:
        return near(x - 2*math.pi)
    else:
        return near(x)

ls = []
for i in range(n):
    point = slist[i]
    r = (point[0]-gs[0])**2+(point[1]-gs[1])**2
    theta = chousei(math.atan2((point[1]-gs[1]),(point[0]-gs[0]))) 
    ls.append([theta,r])
ls.sort()

new_ls = []
for j in range(len(ls)):
    dif = ls[j][0]-ls[j-1][0]
    new_ls.append([chousei(dif),ls[j][1]])
#print(new_ls)



lt = []
for i in range(n):
    point = tlist[i]
    r = (point[0]-gt[0])**2+(point[1]-gt[1])**2
    theta = chousei(math.atan2((point[1]-gt[1]),(point[0]-gt[0])))
    lt.append([theta,r])
lt.sort()

new_lt = []
for j in range(len(lt)):
    dif = lt[j][0]-lt[j-1][0]
    new_lt.append([chousei(dif),lt[j][1]])
#print(new_lt)

new_ls.sort()
new_lt.sort()

def judge(z,w):
    res = True
    for l in range(len(z)):
        if abs(z[l][0]-w[l][0]) > 1e-10:
            res = False
        if abs(z[l][1]-w[l][1]) > 1e-20:
            res = False
    return res

#print(new_ls,new_lt)

if judge(new_ls,new_lt):
    ans = "Yes"
else:
    ans = "No"

print(ans)

