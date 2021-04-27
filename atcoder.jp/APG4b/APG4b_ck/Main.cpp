#include <bits/stdc++.h>
using namespace std;
 
int main() {
  string S;
  cin >> S;
  int val = 1;
  for (int i = 0;i<S.size();i++){
    if (S.at(i)=='+'){
      val++;
    }
    else if (S.at(i)=='-'){
      val--;
    }
  }
  cout << val << endl;
}