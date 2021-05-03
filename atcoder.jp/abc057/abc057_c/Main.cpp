#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(x) (x).begin(),(x).end()
#define int long long
#define ZERO(x) memset(x,0,sizeof(x))
#define print(x) cout << x << endl;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }


signed main(){
    int n,ans=1e18;cin >> n;rep(i,(int)sqrt(n))if (!(n%(i+1)))ans=min(ans,(int)(to_string(n/(i+1)).size()));print(ans)
}