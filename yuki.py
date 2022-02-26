n = int(input())
a = list(map(int,input().split()))
e = 1000000007
alist = []
three = []
temp = 1
th = 1
for i in range(n):
    #temp = temp*a[i]
    #alist.append(temp)
    three.append(th)
    th = th*3%e

#print(three)

ans = 0
for j in range(n-1):
    temp = temp*a[j]%e
    ans += (temp*2*three[n-2-j])%e 
temp = temp*(a[n-1]%e)%e
ans = (ans+temp)%e

print(ans)