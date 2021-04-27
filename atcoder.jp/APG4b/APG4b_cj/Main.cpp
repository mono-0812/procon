#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n = 0;
  cin >> n;
  vector<int> A(n);
  int total=0;
  for (int i;i<n;i++){
    int j = 0;
    cin >> j;
    total+=j;
    A.at(i)=j;
  }
  int ave = total / n;
  for (int i=0;i<n;i++){
    if (A.at(i)>ave){
      cout << A.at(i)-ave << endl;
    }else{
      cout << ave-A.at(i) << endl;
    }
  }
}