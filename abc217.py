import bisect
l,q = map(int,input().split())

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        tmp = array[i] # 挿入する値を退避
        if tmp < array[i-1]:
            # 挿入する位置までずらしていく
            j = i
            while True:
                array[j] = array[j-1]
                j -= 1
                if j == 0 or tmp >= array[j-1]:
                    break
            array[j] = tmp # 
            
h = [0,l]
ans = []
query=[]
for _ in range(q):
    c,x = map(int,input().split())
    query.append([c,x])
    if c == 1:
        h.append(x)
query.reverse()
print("q",query)

h.sort()
print("h",h)

for item in query:
    c,x = item[0],item[1]
    if c == 1:
        #追加
        bisect.insort(h,x)#logn+n
        #print(h)
    else:
        #前後の差を出力
        index = bisect.bisect(h,x)#logn
        res = h[index]-h[index-1]#1
        ans.append(res)

for item in ans:
    print(item)


#include <iostream>
#include <vector>

using namespace std;

int main() {
    int L, Q;
    cin >> L >> Q;
    int c,x;
	vector<int> vector(Q);
	for (int i { 0 }; i < Q; ++i) {
		cin >> d;
		D.push_back(d);
        cin >> c >> x;
        if (c==1){
            index = upper_bound(vector.begin(),vector.end(),a)-vector.begin()
            

        } else {
            index = upper_bound(vector.begin(),vector.end(),a)-vector.begin()
            cout <<  h[index]-h[index-1]
        }
	}
}
