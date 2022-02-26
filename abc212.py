# n,m = map(int,input().split())
# alist = list(map(int,input().split()))
# blist = list(map(int,input().split()))
# alist.sort()
# blist.sort()

# i = 0
# j = 0
# temp = abs(alist[i]-blist[j])
# while True:
#     if i == len(alist)-1 or j == len(blist)-1:
#         break
#     if alist[i] > blist[j]:
#         j += 1
#     else:
#         i += 1
    
#     dif = abs(alist[i] - blist[j])
#     if temp > dif:
#         temp = dif
# print(temp)

#from collections import deque
import heapq
balls = []
add = 0
q = int(input())
qlist = []
for _ in range(q):
    try:
        num,x = map(int,input().split())
        qlist.append([num,x])
    except:
        num = 3
        qlist.append([num,None])
#print(qlist)

addlist = []
add = 0

judge = False
for j in range(q):
    if qlist[j][0] != 2:
        judge = True
    if qlist[j][0] == 2 and judge == True:
        add += qlist[j][1]
    addlist.append(add)
#print(addlist)

for i in range(q):
    if qlist[i][0] == 1:
        #print("==============")
        #print(balls)
        heapq.heappush(balls,qlist[i][1])
        #heapq.heapify(balls)
        #print(balls)
        #print("==============")
    # elif num == 2:
    #     if balls != []:
    #         add += x
    elif qlist[i][0] == 3:
        #num = 3
        #x = None
        if balls != []:
            minimum = heapq.heappop(balls)
            heapq.heapify(balls)
            print(minimum+addlist[i])
        

    


