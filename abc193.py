# import math
# n = int(input())


# def pi(A):
#     pn=[2]
#     for L in range(3,A+1):
#         chk=True
#         for L2 in pn:
#             if L%L2 == 0:chk=False
#         if chk:pn.append(L)
#     return pn

# limit = int(math.sqrt(n))
# kouho = []
# for i in range(2, limit+1):
#     m = int(math.log(n,i))
#     for prime in pi(m):
#         kouho.append(i**prime)
# #print(kouho)

# sum = len(set(kouho))
# print(n-sum)
import random
from collections import Counter

k = int(input())
s = input()
t = input()
remain = [0,k,k,k,k,k,k,k,k,k]
card = []


for i in range(4):
    remain[int(s[i])] = remain[int(s[i])]-1

for i in range(4):
    remain[int(t[i])] = remain[int(t[i])]-1

for l in range(1,10):
    for _ in range(remain[l]):
        card.append(l)

def calc(ls):
    score = 0
    for j in range(1,10):
        score += j*(10**ls.count(j))
    return score

a = 100000
win = 0
for _ in range(a):
    choice = random.sample(card,2)
    s = s[:4] + str(choice[0])
    t = t[:4] + str(choice[1])
    s1 = [int(s[i]) for i in range(5)]
    t1 = [int(t[i]) for i in range(5)]
    if calc(s1) > calc(t1):
        win += 1

print(win/a)