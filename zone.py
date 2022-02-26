# n = int(input())
# member = []
# for _ in range(n):
#     member.append(list(map(int,input().split())))
# from itertools import combinations
# l = [x for x in range(n)]
# cl = combinations(l,3)

# sougou = 0
# for v in cl:
#     a = max(member[v[0]][0],member[v[1]][0],member[v[2]][0])
#     b = max(member[v[0]][1],member[v[1]][1],member[v[2]][1])
#     c = max(member[v[0]][2],member[v[1]][2],member[v[2]][2])
#     d = max(member[v[0]][3],member[v[1]][3],member[v[2]][3])
#     e = max(member[v[0]][4],member[v[1]][4],member[v[2]][4])
#     #print(v,[a,b,c,d,e])
#     temp = min([a,b,c,d,e])
#     if sougou < temp:
#         sougou = temp
# print(sougou)
# print(3000*2999*2888/6)

n = int(input())
member = []
for _ in range(n):
    member.append(list(map(int,input().split())))

member = sorted(member, reverse=True, key=lambda x: max(x))
print(member)

def calc(member):
    a = max(member[0][0],member[1][0],member[2][0])
    b = max(member[0][1],member[1][1],member[2][1])
    c = max(member[0][2],member[1][2],member[2][2])
    d = max(member[0][3],member[1][3],member[2][3])
    e = max(member[0][4],member[1][4],member[2][4])
    score = min([a,b,c,d,e])
    return score

first = member[0]
second = member[1]
third = member[2]
zantei = calc([member[0],member[1],member[2]])

for i in range(3,n):
    new = member[i]
    temp1 = calc([new,second,third])
    temp2 = calc([first,new,third])
    temp3 = calc([first,second,new])
    m = min(temp1,temp2,temp3)
    if m > zantei:
        zantei = m
        if m == temp1:
            first = new
        elif m == temp2:
            second = new
        else:
            third = new
    print(zantei,first,second,third)
print(zantei)



