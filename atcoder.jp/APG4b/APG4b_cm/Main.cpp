#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int A,B;
  cin >> A >> B;
  int i = 0;
  string s;
  while (i<A){
    s+="]";
    i++;
  }
  cout << "A:" << s << endl;
  s = "";
  i = 0;
  while (i<B){
    s+="]";
    i++;
  }
  cout << "B:" << s << endl;
}