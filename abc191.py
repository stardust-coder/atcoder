# n,x = map(int,input().split())
# alist = list(map(int,input().split()))
# ans = ""
# for a in alist:
#     if a != x:
#         ans = ans + str(a) + " "
# print(ans)

#h,w = map(int,input().split())

import math
from decimal import Decimal

x,y,r = map(float,input().split())
count = 0
xleft = x - r
xright = x + r
#print(xleft,xright)
for i in range(math.ceil(xleft),math.floor(xright)+1):
    #print(i)
    width = math.sqrt(r**2 - abs(x-i)**2)
    yup = y + width
    ydown = y - width
    plus = math.floor(yup) - math.ceil(ydown) + 1
    count += plus
    if (math.floor(yup)+1 - y)**2 + (i - x)**2 == r**2:
        count += 1
    if (math.ceil(ydown)-1 - y)**2 + (i - x)**2 == r**2:
        count += 1

print(count)

