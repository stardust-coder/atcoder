# a,b,k = map(int,input().split())

# import math
# def combinations_count(n, r):
#     return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))

# def calc(a,b):
#     sum =  combinations_count(a+b,a)
#     return int(sum)

# res = ""
# remain_a = a
# remain_b = b
# remain_k = k
# for _ in range(a+b):
#     #print(remain_a,remain_b)
#     if remain_a == 0:
#         res = res + "b"*remain_b
#         break
#     elif remain_b == 0:
#         res = res + "a"*remain_a
#         break
#     else:
#         border = calc(remain_a-1,remain_b)
#         if  border < remain_k:
#             res = res + "b"
#             remain_b -= 1
#             remain_k -= border
#         else:
#             res = res + "a"
#             remain_a -= 1
#     #print(res)
# print(res)

# n = int(input())
# point_list = []
# for _ in range(n):
#     point_list.append(list(map(int,input().split())))
# print(point_list)

N = int(input())
parents = list(map(int,input().split()))
p = [[] for _ in range(N+1)]
for i in range(len(parents)):
    p[parents[i]].append(i+2)
print(p)
q = int(input())

class Node:
    def __init__(self):
        self.parent = -1
        self.children = []

def cal_depth(node_id, d = 0):
    Tree[node_id].depth = d
    for child in Tree[node_id].children:
        cal_depth(child, d+1)
    
Tree = [Node() for _ in range(N+1)]

#make_tree
for l in range(1,N+1):
    #id, 子供の数k, c_0~c_k
    tree_info = [l,len(p[l])]+p[l]
    node_id = tree_info[0]
    k = tree_info[1]
    if k > 0:
        children = tree_info[2:]
        Tree[node_id].children = children
        Tree[node_id].type = "internal node"
    else:
        Tree[node_id].type = "leaf"
        
    for child in Tree[node_id].children:
        Tree[child].parent = node_id

#search_root
root_id =[i for i,t in enumerate(Tree) if t.parent == -1][0]
Tree[root_id].type = "root"
cal_depth(root_id)


#answer_output
for i, t in enumerate(Tree):
    print("node {}: parent = {}, depth = {}, {}, {}".format(i, t.parent, t.depth, t.type, t.children))
