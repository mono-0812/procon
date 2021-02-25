#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    int n;
    cin >> n;
    vector<int> L(n);
    int ans=0;
    rep(i,n){
        cin >> L.at(i);
    }
    sort(L.begin(),L.end());
    rep(i,n)rep(j,n)rep(k,n){
        
        if(L.at(k)<L.at(j)+L.at(i) && L.at(i)!=L.at(j) && L.at(j)!=L.at(k) && L.at(i)!=L.at(k) && k>j && j>i){
            ans++;
        }
    }
    cout << ans << endl;
}