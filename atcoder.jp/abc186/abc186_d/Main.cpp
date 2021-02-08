#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main(){
  int n=0;
  long long ans = 0LL;
  long long sum = 0LL;
  cin >> n;
  vector<long long> A(n);
  rep (i,n)cin >> A.at(i);
  sort(A.begin(),A.end());
  rep (i,n){
    sum+=A[i];
    ans-=sum;
    ans += A[i]*(i+1);
  
    
    
  }
  cout << ans << endl;
}