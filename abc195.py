# from math import log10,ceil
# n = int(input())
# def full(keta):
#     return (ceil(keta/3)-1)*9*(10**(keta-1))


# num_keta = int(log10(n))+1
# amari = (ceil(num_keta/3)-1)*(n-10**(num_keta-1)+1)
# sum = amari

# for i in range(1,num_keta):
#     sum += full(i)
# print(sum)

# n,m,q = map(int,input().split())
# bag = []
# for _ in range(n):
#     w,v = map(int,input().split())
#     bag.append([w,v])
# xlist = list(map(int,input().split()))
# bag.sort(key=lambda x:x[1],reverse=True)

# for _ in range(q):
#     l,r = map(int,input().split())
#     #print("query")
#     newls = xlist[:l-1]
#     newls[len(newls):len(newls)] = xlist[r:] 
#     newls.sort()
#     #print(newls, bag)
#     sum = 0
#     for item in bag:
#         if newls == []:
#             break
#         index = 0
#         if item[0] <= max(newls):
#             while item[0]>newls[index]:
#                 index += 1
#             sum += item[1]
#             newls.pop(index)
#     print(sum)

#E
n = int(input())
s = input()
x = input()

#DP？
    
