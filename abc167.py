# n,m,x = map(int,input().split())
#
# listA=[] #appendのために宣言が必要
# for _ in range(n):
#     listA.append(list(map(int,input().split())))
#
# kanoucost = []
# for i in range(2**n):
#     ls = [0]*n
#     for j in range(len(ls)):
#         if (i >> j) & 1:
#             ls[j] = 1
#     ability = [0]*(m+1)
#     for k in range(len(ls)):
#         new = [n * ls[k] for n in listA[k]]
#         ability = [x + y for (x, y) in zip(ability, new)]
#
#     if min(ability[1:]) >= x:
#         kanoucost.append(ability[0])
#
# if kanoucost == []:
#     print("-1")
# else:
#     print(min(kanoucost))
#
#167-4
n,k = map(int,input().split())
listA = list(map(int,input().split()))

kouho = [1]
ikisaki = listA[0]
while ikisaki not in kouho:
    kouho.append(ikisaki)
    ikisaki = listA[ikisaki-1]

index = kouho.index(ikisaki)
loop = len(kouho) - index
amari = (k-index)%loop
print(kouho[index + amari])
