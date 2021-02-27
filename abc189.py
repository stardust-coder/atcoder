n = int(input())
temp = 0
als = list(map(int,input().split()))
# for l in range(n):
#     for r in range(l,n):
#         mini = min(als[l:r+1])
#         if temp < mini*(r-l+1):
#             temp = mini*(r-l+1)
#         #print(l,r,temp)

# print(temp)



def mikan(ls):
    if ls == []:
        return 0
    else:
        return min(ls)*len(ls)

l = 0
r = 0
temp = mikan(als[l:r+1])
kouhols = []
while r != n:
    #print(l,r)
    kouho1 = mikan(als[l:r+2])
    kouho2 = mikan(als[l+1:r+1])
    #print(kouho1,kouho2,temp)
    if kouho1 > temp:
        r += 1
        temp = kouho1
    elif kouho2 > temp:
        l += 1
        temp = kouho2
    else:
        kouhols.append(temp)
        l += 1
        r += 1
        temp = 0

print(max(temp,max(kouhols)))


# n = int(input())
# ls = []
# for _ in range(n):
#     s = input()
#     ls.append(s)

# def num(i):#y_iがTrueの個数
#     if i == 0:
#         return 1,1
#     else:
#         pre = num(i-1)
#         if ls[i-1] == "AND":
#             t = pre[0]*1
#             f = pre[0]*1 + pre[1]*2
#         else:      
#             t = pre[0]*2 + pre[1]*1
#             f = pre[1]*1 
#         return t,f

# print(num(n)[0])

# n = int(input())
# cor = []
# for _ in range(n):
#     cor.append(list(map(int,input().split())))
# m = int(input())
# sousa = []
# for _ in range(m):
#     sousa.append(list(map(int,input().split())))
# q = int(input())
# qls = []
# for i in range(q):
#     a,b = map(int,input().split())
#     qls.append([i,a,b])
# sorteda = sorted(qls,key=lambda x: x[1])

# def one():
#     print("one")
# def two():
#     print("two")
# def three(p):
#     print("three","p",p)
# def four(p):
#     print("four","p",p)

# ans = []
# aindex = 0

# for i in range(m):
#     while sorteda[aindex][1] == i:
#         ans.append(cor[sorteda[aindex][2]-1])
#         aindex += 1
#         print(i)
#     sou = sousa[i]
#     if sou[0] == 1:
#         one()
#     elif sou[0] == 2:
#         two()
#     elif sou[0] == 3:
#         three(sou[1])
#     else:
#         four(sou[1])  
    
# print(ans)

