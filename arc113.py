# import math
# k = int(input())

# first = 0
# for a in range(1,math.ceil(k**(1/3))):
#     for b in range(a+1,math.ceil(math.sqrt(k/a))):
#         first += int(k/(a*b))-b
# #print(first)

# third = math.floor(k**(1/3))
# #print(third)

# second = 0
# for d in range(1,math.floor(k**(1/2))+1):
#     second += int(k/(d**2))
# second -= third
# #print(second)

# print(first*6+second*3+third*1)

#B
# a,b,c = map(int,input().split())
# if c == 1:
#     temp = ((a%10)**(4+b%4))%10
# else:
#     if b%4 == 1:
#         b4 = 1
#     elif b%4 == 3:
#         if c %2 == 0:
#             b4 = 1
#         else:
#             b4 = 3
#     else:
#         b4 = 0
#     temp = ((a%10)**(4+b4))%10
# print(temp)

#C
s = input()
collect = []

for i in range(len(s)-2):
    if s[i] == s[i+1] and s[i+1]!=s[i+2]:
        collect.append([s[i],i])

sum = 0
n = len(s)
collect.append(["str",len(s)])
for j in range(len(collect)-1):
    #print("j",j)
    new =  n-collect[j][1]-2
    red = s[collect[j][1]+2:collect[j+1][1]].count(collect[j][0])
    new -= red
    #print(j,red)
    if collect[j][0] == collect[j+1][0]:
        new -= n-collect[j+1][1]
    sum += new
print(sum)



