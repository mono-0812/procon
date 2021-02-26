#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    string s; string t;
    int ans = 0;
    cin >> s >> t;
    rep(i,s.size()){
        if(s[i]!=t[i]){
            ans++;
        }
    }
    cout << ans << endl;
}