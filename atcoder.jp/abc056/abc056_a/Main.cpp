#include <bits/stdc++.h>
using namespace std;
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(x) (x).begin(),(x).end()
#define ZERO(x) memset(x,0,sizeof(x))
#define print(x) cout << x << endl;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using pint = pair<int,int>;
int gcd(int x, int y) {
    while (y > 0) {
        int r = x % y;
        x = y;
        y = r;
    }
    return x;
}
signed main(){
    char a,b;
    cin >> a >> b;
    if (a==b)cout<<"H"<<endl;
    else cout<<"D"<<endl;
}