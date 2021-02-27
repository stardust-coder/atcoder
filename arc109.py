# a,b,x,y = map(int,input().split())
#
# if 2*x < y:
#     if a>b:
#         res = (abs(b-a)*2-1)*x
#     else:
#         res = (abs(b-a)*2+1)*x
# else:
#     if a>b:
#         res = x + (abs(b-a)-1)*y
#     else:
#         res = x + abs(b-a)*y
# print(res)

# import math
# import decimal
#
# n = int(input())
# k = 0
#
# a = decimal.Decimal(math.sqrt(2*(n+1)))
# temp = a.quantize(decimal.Decimal("1"), rounding=decimal.ROUND_FLOOR)+1
# while (temp+1)*temp/2 > n+1:
#     temp -= 1
#
# print(n-temp+1)

#C
#
# n,k = map(int,input().split())
# s = input()
#
# # if 2**k <= n:
# #     text = s[:2**k]
# # elif n%2 == 1:
# #     text = (s + s)[:2**k]
# # else:
# #     text = s
# #print(text)
#
# def jyanken(a,b):
#     if (a,b) in [("R","S"),("S","R"),("R","R")]:
#         return "R"
#     if (a,b) in [("R","P"),("P","R"),("P","P")]:
#         return "P"
#     if (a,b) in [("P","S"),("S","P"),("S","S")]:
#         return "S"
#
# def step(text):
#     res = ""
#     for i in range(0,len(text),2):
#         res = res + jyanken(text[i],text[i+1])
#     return res
#
# text = s
# ktemp = k
# while len(text) != 1:
#     if 2**ktemp <= len(text):
#         text = text[:2**ktemp]
#     elif len(text)%2 == 1:
#         temp = (text + text)[:2**ktemp]
#         text = temp
#     text = step(text)
#     ktemp -= 1
#
# print(text)

#D
T = int(input())
caselist = []
for _ in range(T):
    case = list(map(int,input().split()))
    caselist.append(case)
#print(caselist)

def dis(x,y):
    return abs(x)+abs(y)

for case in caselist:
    points = [(case[0],case[1]),(case[2],case[3]),(case[4],case[5])]
    tate = max(abs(case[1]),abs(case[3]),abs(case[5]))
    yoko = max(abs(case[0]),abs(case[2]),abs(case[4]))
    res = tate + yoko - 2
    if case[0]+case[2]+case[4] >= 0 and case[1]+case[3]+case[5] >= 0:
        res += 1
    if case[0]+case[2]+case[4] <= 0 and case[1]+case[3]+case[5] <= 0:
        res += 2
    else:
        res += 1
    print(res)
    if (tate,yoko) not in points:
        res += 2
    elif (tate-1,yoko-1) not in points:
        res += 1
