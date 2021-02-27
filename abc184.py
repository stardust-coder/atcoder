# import math
# r1, c1 = map(int,input().split())
# r2, c2 = map(int,input().split())
# tate = abs(r2 - r1)
# yoko = abs(c2 - c1)
#
# if r1 == r2 and c1 == c2:
#     res = 0
# elif r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
#     res = 1
# elif abs(abs(r1-r2)-abs(c1-c2)) <= 3:
#     res = 2
# elif (tate + yoko)%2 == 0:
#     res = 2
# else:
#     res = 3
#
# print(res)

#D
# import random
# a1,b1,c1 = map(int,input().split())
#
# ls = []
# k = 100000
# for i in range(k):
#     a,b,c = a1,b1,c1
#     count = 0
#     while a<=99 and b <= 99 and c<=99:
#         ran = random.randint(1,a+b+c)
#         if ran <= a:
#             a += 1
#         elif ran <= a+b:
#             b += 1
#         else:
#             c += 1
#         count += 1
#     ls.append(count)
#
# print(sum(ls)/len(ls))


#
# a,b,c = map(int,input().split())
# def expectation(a,b,c):
#     if a >= 100 or b >= 100 or c >= 100:
#         return 1
#     else:
#         res = (a*(expectation(a+1,b,c)+1) + b*(expectation(a,b+1,c)+1) + c*(expectation(a,b,c+1)+1))/(a+b+c)
#         return res
# print(expectation(a,b,c))

# import math
# a,b,c = map(int,input().split())
#
# def permutations_count(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
#
# def fact(m,n):
#     val = 1
#     for i in range(m, n + 1):
#         val *= i
#     return val
#
# ex = 0
#
# x = 100
# for y in range(b,100):
#     for z in range(c,100):
#         #print(x,y,z)
#         prob = fact(a,x)*fact(b,(y-1))*fact(c,(z-1))/(fact(a+b+c,x+y+z-1))
#         all = x-a+y-b+z-c-1
#         route = permutations_count(all,z-c)*permutations_count(all-(z-c),y-b)#x=100ってぜんてい
#         temp = prob*route*(x+y+z-a-b-c)
#         ex += temp
#         #print(ex)
#
# y = 100
# for x in range(a,100):
#     for z in range(c,100):
#         #print(x,y,z)
#         prob = fact(a,x-1)*fact(b,y)*fact(c,(z-1))/(fact(a+b+c,x+y+z-1))
#         all = x-a+y-b+z-c-1
#         route = permutations_count(all,z-c)*permutations_count(all-(z-c),y-1-b)#x=100ってぜんてい
#
#         temp = prob*route*(x+y+z-a-b-c)
#         ex += temp
#
# z = 100
# for y in range(b,100):
#     for x in range(a,100):
#         #print(x,y,z)
#         prob = fact(a,x-1)*fact(b,y-1)*fact(c,z)/(fact(a+b+c,x+y+z-1))
#         all = x-a+y-b+z-c-1
#         route = permutations_count(all,z-1-c)*permutations_count(all-(z-1-c),y-b)#x=100ってぜんてい
#         temp = prob*route*(x+y+z-a-b-c)
#         ex += temp
#
# print(ex/100)

#E
h,w = map(int,input().split())
togoal=[]
for j in range(h):
    s = input()
    ls = []
    for i in range(w):
        if s[i] != "#":
            ls.append(h-j+w-i-2)
        else:
            ls.append(0)
    togoal.append(ls)

print(togoal)
