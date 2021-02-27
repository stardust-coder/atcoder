n = int(input())

if n == 1:
    print(1,1)
elif n == 2:
    print(1,2)
    print(2,1)
else:
    for i in range(1,n+1):
        if i*2 <= n:
            print(i,i*2)
            if i*2+1 <= n:
                print(i,i*2+1)
            else:
                print(i,1)
        else:
            print(i,1)
            print(i,2)

