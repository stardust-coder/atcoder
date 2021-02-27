# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
#
# s,p = map(int,input().split())
# res = False
# for i in make_divisors(p):
#     if s-i == p/i:
#         res = True
# if res == True:
#     print("Yes")
# else:
#     print("No")

#N = int(input())
#s = input()

#
# def countfox(text):
#     res = 0
#     add = 1
#     txt = text
#     while True:
#         newtxt = txt.replace("fox","")
#         if newtxt == txt:
#             return int((len(text) - len(newtxt))/3)
#         txt = newtxt
#
# count = 0
# foxbox = ""
# for i in range(N):
#     if s[i] == "f":
#         foxbox = foxbox + "f"
#     elif foxbox != [] and s[i] == "o":
#         foxbox = foxbox + "o"
#     elif foxbox != [] and s[i] == "x":
#         foxbox = foxbox + "x"
#     else:
#         #print(foxbox)
#         count += countfox(foxbox)
#         foxbox = ""
#     #print(foxbox)
# count += countfox(foxbox)
# ans = N - 3*count
# print(ans)

N = int(input())
s = input()
box = ""
count = 0
for i in range(N):
    box = box + s[i]
    #print(box)
    if box[-3:] == "fox":
        count += 1
        box = box[:-3]
print(N-3*count)
