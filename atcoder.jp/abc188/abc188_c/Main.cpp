#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    int n;
    cin >> n;
    vector<int> A(pow(2,n));
    rep(i,pow(2,n)){cin >> A.at(i);}
    int val1=0;
    int val2=0;
    rep(i,A.size()/2){
        val1=max(val1,A.at(i));
    }
    rep(i,A.size()/2){
        val2=max(val2,A.at(i+A.size()/2));
    }
	int ans=0;
  	rep(i,A.size()){
    	if(A.at(i)==min(val1,val2)){
        	ans=i;
        }
    }  
    cout << ans+1 << endl;
}