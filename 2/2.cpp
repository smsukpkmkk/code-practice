#include<vector>
#include<cstdio>
#include<iostream>
using namespace std;   
int main()
{
    vector<int> a={1,2,3,4,5};
    for(int i=0;i<a.size();i++)
        printf("%d \n",a[i]);
    int n=a.size();
    cout << n << endl;
    return 0;
}