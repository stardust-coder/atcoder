# s = input()#len10
# o = 0
# x = 0
# z = 0
# for i in range(10):
#     if si] == "o":
#         o += 1
#     if s[i] == "x":
#         x += 1
#     if s[i] == "?":
#         z += 1
# #print(o,x,z)

# if o >= 5:
#     res = 0
# elif o == 4:
#     res = 24
# elif o == 3:
#     dif = 4*(3*2*1)*z
#     same = (6*2*1)*3
#     res = dif + same
# elif o == 2:
#     dif = 12*z*z
#     a = 6 + 4*2
#     b = (6*2*z)*2
#     res = dif+a+b
# elif o == 1:
#     four = 1
#     three = 4*z
#     two = 6*z*z
#     one = 4*z*z*z
#     res = four+three+two+one
# else:
#     res = z*z*z*z
# print(res)

#D
h,w = map(int,input().split())
mat = []
for _ in range(h):
    s = input()
    row = []
    for k in range(w):
        if s[k]=="+":
            row.append(1)
        else:
            row.append(-1)
    mat.append(row)

#print(mat)
def score(i,j):
    if i==h-1 and j==w-1:
        return 0
    elif (i+j)%2==0:
        #高橋くんの番
        if i==h-1:
            return score(i,j+1)+mat[i][j+1]
        elif j==w-1:
            return score(i+1,j)+mat[i+1][j]
        else:
            return max(score(i,j+1)+mat[i][j+1],score(i+1,j)+mat[i+1][j])
    else:
        #青木くんの番
        if i==h-1:
            return score(i,j+1)-mat[i][j+1]
        elif j==w-1:
            return score(i+1,j)-mat[i+1][j]
        else:
            return min(score(i,j+1)-mat[i][j+1],score(i+1,j)-mat[i+1][j])

sc = score(0,0)
if sc == 0:
    print("Draw")
elif sc > 0:
    print("Takahashi")
else:
    print("Aoki")

#E
# n = int(input())
# graph = []
# for _ in range(n-1):
#     graph.append(list(map(int,input().split())))

