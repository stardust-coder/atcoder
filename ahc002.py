si,sj = map(int,input().split())
tiles = []
points = []
index = [[] for _ in range(2500)]

for i in range(50):
    ls = list(map(int,input().split()))
    for j in range(len(ls)):
        index[ls[j]].append([i,j])
    tiles.append(ls)
#print(tiles)
for _ in range(50):
    ls = list(map(int,input().split()))
    points.append(ls)
#print(points)

import random
def step(now):
    possible = []
    #tilenum = tiles[now[0]][now[1]]
    if now[0] != 0:
        up = [now[0]-1,now[1]]
        upnum = tiles[up[0]][up[1]]
        if upnum not in visited:
            possible.append(0)
    if now[0] != 49:
        down = [now[0]+1,now[1]]
        downnum = tiles[down[0]][down[1]]
        if downnum not in visited:
            possible.append(1)
    if now[1] != 0:
        left = [now[0],now[1]-1]
        leftnum = tiles[left[0]][left[1]]
        if leftnum not in visited:
            possible.append(2)
    if now[1] != 49:
        right = [now[0],now[1]+1]
        rightnum = tiles[right[0]][right[1]]
        if rightnum not in visited:
            possible.append(3)
    
    if possible == []:
        return False,False

    else:
        dec = random.choice(possible)   
        if dec == 0:
            visited.append(upnum)
            return "U",up
        elif dec == 1:
            visited.append(downnum)
            return "D",down
        elif dec == 2:
            visited.append(leftnum)
            return "L",left
        else:
            visited.append(rightnum)
            return "R",right




kouho = {}
for _ in range(10000):
    now = [si,sj]
    #print("now",now)
    ans = ""
    score = points[si][sj]
    visited = [tiles[now[0]][now[1]]]
    for _ in range(2500):
        res,now = step(now)
        #print("now",now)
        if res == False:
            break
        else:
            score += points[now[0]][now[1]]
            ans = ans + res
    #print(ans,score)
    kouho[ans] = score

max_k = max(kouho,key=kouho.get)
print(max_k)



    
    
