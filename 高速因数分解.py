n = int(input())
D = [0,1]#D[i]はiを割り切る最小の素数
for i in range(2,n+1):
    if i % 2 == 0:
        D.append(2)
    else:
        D.append(0)


prime = [2]
limit = int(n**0.5)
data = [i+1 for i in range(2,n,2)]
while data != []:
    p = data[0]
    prime.append(p)
    #print("prime",prime)
    for item in data:
        if item%p == 0:
            D[item] = p
            data.remove(item)

print(prime)
print(D)
