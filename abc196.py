import math
h,w,a,b = map(int,input().split())

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

tate = min(h,w)
yoko = max(h,w)

if tate == 1:
    bunkatu = [1]
elif tate == 2:
    bunkatu = [[2],[1,1]]
elif tate == 3:
    bunkatu = [[3],[2,1],[1,2],[1,1,1]]
elif tate == 4:
    bunkatu = [[4],[3,1],[1,3],[2,2],[2,1,1],[1,2,1],[1,1,2],[1,1,1,1]]

def one(l,a):
    return combinations_count(a+(l-2*a),a)

def two(l,a):
    if l<a:
        return 0
    elif l == 2:
        if a == 2:
            return 2
        elif a == 1:
            return 4
    elif a == 0:
        return 1
    elif l==1:
        return 1
    elif a == 1:
        return (l-1)*2+l
    else:
        print(two(l-1,a),two(l-1,a-1),two(l-2,a-1),two(l-2,a-2))
        return max(0,two(l-1,a) + two(l-1,a-1) + two(l-2,a-1)*2 + two(l-2,a-2)*2)

def three(l,a):
    if 3*l < 2*a:
        return 0
    elif a == 0:
        return 1
    elif l == 1:
        return 2 
    elif l == 2:
        if a == 3:
            return 3
        elif a == 2:
            return 4
        elif a == 1:
            return 7
    elif l == 3:
        return 18
    elif l == 4:
        res = three(l-1,a) + three(l-1,a-1)*2 + three(l-2,a-1)*3 + three(l-2,a-2)*7 + three(l-2,a-3)
        return max(0,res)

def four(l,a):
    if 4*l < 2*a:
        return 0
    elif a == 0:
        return 1
    elif l == 1:
        if a == 2:
            return 1
        elif a == 1:
            return 3
    elif l == 2:
        if a == 4:
            return 5
        elif a == 3:
            return two(4,3)
        elif a == 2:
            return two(4,2)
        elif a == 1:
            return 10
    else:
        res = four(l-1,a) + four(l-1,a-1)*3 + four(l-1,a-2)*1 + four(l-2,a-1)*4 + four(l-2,a-2)*6  + four(l-2,a-3)*4 + four(l-2,a-4)*1
        return max(0,res)


print(four(4,8))