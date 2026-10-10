#include <bits/stdc++.h>
using namespace std;

int main()
{
  map<int , int> mp;

  for(int i= 0; i < 5; i++)
  {
    int x;
    cin>>x;
    mp[i] = x;
  }

  for(auto p: mp)
  {
    cout<<p.first<<" "<<p.second++<<endl;


    
  }


}