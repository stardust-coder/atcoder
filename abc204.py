n = int(input())
t = list(map(int,input().split()))
t.sort(reverse=True)
a = 0
b = 0
for i in range(len(t)):
    if a > b:
        b += t[i]
    else:
        a += t[i]
kouho1 = max(a,b)

