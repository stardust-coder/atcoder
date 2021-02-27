# t = int(input())
# for _ in range(t):
#     l,r = map(int,input().split())
#     if l*2 > r:
#         print(0)
#     else:
#         print(int((r-2*l+2)*(r-2*l+1)/2))

b,c = map(int,input().split())

if b < 0:
    print(int(c/2)+1+max(min(c-1,2*abs(b)-1),0)+int((c+1)/2))
elif b > 0:
    print(1+int((c+1)/2)+max(min(c,2*abs(b)-1),0)+max(0,int((c-2)/2)))
elif c == 0:
    print(1)
else:
    print(c)


