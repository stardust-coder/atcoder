#A
# s = input()
# t = input()
# if s == t:
#     print("same")
# elif s.lower() == t.lower():
#     print("case-insensitive")
# else:
#     print("different")

#B
# n,m,q = map(int,input().split())
# acs = []
# for _ in range(n):
#     acs.append([])
# acpoints = [n]*n
#
# def queryone(query):
#     person = query[1]
#     aclist = acs[person-1]
#     sum = 0
#     for ac in aclist:
#         sum += acpoints[ac-1]
#     print(sum)
#
# def querytwo(query):
#     acperson = query[1]
#     acquestion = query[2]
#     acpoints[acquestion-1] -= 1
#     acs[acperson-1] += [acquestion]
#
# inputquery = []
# for _ in range(q):
#     inputquery.append(list(map(int,input().split())))
#
# for query in inputquery:
#     if query[0] == 1:
#         queryone(query)
#     else:
#         querytwo(query)

#C
# import math
# a,r,n = map(int,input().split())
# if r==1:
#     print(a)
# else:
#     kijun = math.log(10**9/a)/math.log(r)
#     if n > kijun+1:
#         print("large")
#     else:
#         print(a*(r**(n-1)))

#I
# import numpy as np
# n = int(input())
# q = int(input())
# w = np.ones((n,n), dtype="int64")
# for i in range(n):
#     w[i] = w[i]*i
# matrix = n*w + w.T
# np.int64(matrix)
#
# def queryone(matrix,query):
#     a = query[1]-1
#     b = query[2]-1
#     matrix[a], matrix[b]= matrix[b], matrix[a].copy()
#     return matrix
#
# def querytwo(matrix,query):
#     a = query[1]-1
#     b = query[2]-1
#     matrixtranspose = matrix.T
#     matrixtranspose[a], matrixtranspose[b]= matrixtranspose[b], matrixtranspose[a].copy()
#     matrix = matrixtranspose.T
#     return matrix
#
# def querythree(matrix):
#     matrix = matrix.T
#     return matrix
#
#
# def queryfour(matrix,query,answer):
#     a = query[1]-1
#     b = query[2]-1
#     answer.append(matrix[a][b])
#
# answer = []
# for _ in range(q):
#     query = list(map(int,input().split()))
#     if query[0] == 1:
#         matrix = queryone(matrix,query)
#     if query[0] == 2:
#         matrix = querytwo(matrix,query)
#     if query[0] == 3:
#         matrix = querythree(matrix)
#     if query[0] == 4:
#         queryfour(matrix,query,answer)
#
# for ans in answer:
#     print(ans)

#F回文行列
# n = int(input())
# char = []
# for _ in range(n):
#     char.append(input())
#
# ans = 0
# answerlist = []
# for i in range(int(n/2)):
#     text1 = list(char[i])
#     text2 = list(char[-i-1])
#     commonset = set(text1) & set(text2)
#     common = list(commonset)
#     if len(common) == 0:
#         ans = -1
#         break
#     else:
#         answerlist.append(common[0])
#
# if ans == -1:
#     print(-1)
# else:
#     newlist = list(reversed(answerlist))
#     if n%2 == 1:
#         answerlist.append(char[int((n-1)/2)][0])
#     answerlist.extend(newlist)
#     mojiretsu = "".join(answerlist)
#     print(mojiretsu)

#N
# n,q = map(int,input().split())
#
# def queryone(suuretu,query):
#     x = query[1]-1
#     suuretu[x], suuretu[x+1] = suuretu[x+1], suuretu[x]
#     return suuretu
#
# def querytwo(suuretu,query):
#     x = query[1]-1
#     y = query[2]-1
#     list1 = suuretu[:x]
#     list2 = suuretu[x:y+1]
#     list3 = suuretu[y+1:]
#     list2.sort()
#     list1.extend(list2)
#     list1.extend(list3)
#     return list1
#
# suuretu = [i for i in range(1,n+1)]
# for _ in range(q):
#     query = list(map(int,input().split()))
#     if query[0] == 1:
#         suuretu = queryone(suuretu,query)
#     if query[0] == 2:
#         suuretu = querytwo(suuretu,query)
#
# print(" ".join(map(str,suuretu)))

#D電光掲示板
# def read_number(ls):
#     if ls == [".###",".#.#",".#.#",".#.#",".###"]:
#         return 0
#     if ls == ["..#.",".##.","..#.","..#.",".###"]:
#         return 1
#     if ls == [".###","...#",".###",".#..",".###"]:
#         return 2
#     if ls == [".###","...#",".###","...#",".###"]:
#         return 3
#     if ls == [".#.#",".#.#",".###","...#","...#"]:
#         return 4
#     if ls == [".###",".#..",".###","...#",".###"]:
#         return 5
#     if ls == [".###",".#..",".###",".#.#",".###"]:
#         return 6
#     if ls == [".###","...#","...#","...#","...#"]:
#         return 7
#     if ls == [".###",".#.#",".###",".#.#",".###"]:
#         return 8
#     if ls == [".###",".#.#",".###","...#",".###"]:
#         return 9
# n = int(input())
# sdata = []
# answerlist = []
# for _ in range(5):
#     sdata.append(input())
# for i in range(n):
#     compare = []
#     for j in range(5):
#         compare.append(sdata[j][i*4:(i+1)*4])
#     ans = read_number(compare)
#     answerlist.append(ans)
# print("".join(map(str,answerlist)))

#E
n,m,q = map(int,input().split())
rinsetu = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    rinsetu[u-1].append(v-1)
    rinsetu[v-1].append(u-1)
colorlist = list(map(int,input().split()))
ans = []
def queryone(query):
    x = query[1]-1
    ans.append(colorlist[x])
    for int in rinsetu[x]:
        colorlist[int] = colorlist[x]

def querytwo(query):
    x = query[1]-1
    y = query[2]
    ans.append(colorlist[x])
    colorlist[x] = y

for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        queryone(query)
    if query[0] == 2:
        querytwo(query)

for j in range(q):
    print(ans[j])
