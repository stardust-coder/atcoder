#1
# k = int(input())
# a,b = map(int,input().split())
# if b-a+1 >= k or a % k == 0 or b % k == 0:
#     print("OK")
# elif a%k > b%k:
#     print("OK")
# else:
#     print("NG")

#2
# import math
# x = int(input())
# count = 0
# now = 100
# while(now < x):
#     now += math.floor(now*0.01)
#     count += 1
# print(count)

#4

import math
a,b,n = map(int,input().split())

if b <= n:
    k = math.floor(n/b)
    ans = max(math.floor(a*(b-1)/b), math.floor(a*n/b)- a*math.floor(n/b),math.floor(a*(k*b-1)/b)-a*math.floor((k*b-1)/b))
    print(ans)
else:
    print(math.floor(a*n/b))
