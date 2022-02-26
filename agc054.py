#A
# n = int(input())
# s = input()

# sentou = s[0]

# if s[0] != s[-1]:
#     print(1)
# else:
#     res = False
#     for i in range(1,len(s)-1):
#         if s[i] != sentou:
#             if s[i-1]!=sentou or s[i+1]!=sentou:
#                 res = True
#     if res == True:
#         print(2)
#     else:
#         print(-1)

#D
s = input()
onum,xnum,lnum,rnum = 0,0,0,0
for i in range(len(s)):
    if s[i] == "o":
        onum += 1
    if s[i] == "x":
        xnum += 1
    if s[i] == "(":
        lnum += 1
    else:
        rnum += 1 


def dp(i):
    if i==1:
        if s[i] == "(":
            return 1
        else:
            return 0
    else:
        
