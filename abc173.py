# import numpy as np
# h,w,k = map(int,input().split())
# masu = []
# for i in range(h):
# 	masu.append(list(map(str,input().split())))
#
# op_cnt = h  # すき間の個数
# ophlist = []
# opwlist = []
# for i in range(2 ** op_cnt):
#     op_h = [0] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
#     for j in range(op_cnt):
#         if ((i >> j) & 1):
#             op_h[op_cnt - 1 - j] = 1
# 			ophlist.append(op_h)
#
# op_cnt = w  # すき間の個数
# for i in range(2 ** op_cnt):
#     op_w = [0] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
#     for j in range(op_cnt):
#         if ((i >> j) & 1):
#             op_w[op_cnt - 1 - j] = 1
# 			opwlist.append(op_w)
#
# for oph in ophlist:
# 	for opw in opwlist:
# 		harray = np.array([oph])
# 		warray = np.array([opw])
# 		x = np.dot(harray.T,warray)
# 		print(harray, warray ,x)


# n = int(input())
# comfort = 0
# alist = list(map(int,input().split()))
# alist.sort(reverse = True)
# comfort += alist[0]
# for i in range(1,int(n/2)):
# 	comfort += alist[i]*2
# if n%2 ==1:
# 	comfort += alist[int((n-1)/2)]
# print(comfort)

n,k = map(int,input().split())
alist = list(map(int,input().split()))
sorted = sorted(alist, key = abs, reverse=True)
print(sorted)

kouhoa = 1
kouhob = 1
fugou = 0
for i in range(k):
	kouhoa *= sorted[i]
	kouhob *= sorted[-i-1]
	if sorted[i] > 0:
		fugou +=1

if fugou == 0:
	print(kouhob)
else:
	kouhoa * 
	print(kouhoa)
