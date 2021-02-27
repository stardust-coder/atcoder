#スタックとキュー
from collections import deque#O(1)でpopできる
s = deque([])
s.append(1)
s.pop()
q = deque([])
q.append(1)
q.popleft()

#多次元リストのsort
from operator import itemgetter
st = sorted([[1,6,7],[2,5,8],[3,4,9]],key = itemgetter(1))
print(st)


#ビット演算
print(0b101)
print(bin(5))
print(0x12)
print(hex(0b10010))
print(bin(5<<1))
print(bin(5>>1))
#ANDは&, ORは|, XORは^, NOTは~
print(bin(0b101110&0b000111))#ビットマスク, 必要な部分だけ1にしてAND
print(bin(0b101^0b010))#XORでまちがいさがしができる

#二分ヒープ
import heapq
a = [1,2,3,4,5]#既存リスト
heapq.heapify(a)#リスト->優先度付きキュー
print(a)
heapq.heappop(a)#最小値の取り出しO(1) #最大値は-1倍を活用
print(a)
heapq.heappush(a,-2)#要素の挿入O(logN)
print(a)
heapq.heappushpop(a,6)#xを追加したのち最小値をpop
print(a)

#セグメント木
class SegmentTree:
    def __init__(self,n,ele=10**10):

        self.ide_ele = ele

        self.num =2**(n-1).bit_length()
        self.seg=[self.ide_ele]*2*self.num


    #####segfunc######
    def segfunc(self,x,y):
        return min(x,y)

    def init(self,init_val):
        #set_val
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i]
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2])

    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])

    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

def power(x,n,MOD):
    ret = 1
    while n>0:
        if n%2==1:
            ret*=x
            ret%=MOD
        x*=x
        x%=MOD
        n/=2
    return ret

def modinv(x,MOD):
    return power(x,MOD-2,MOD)
