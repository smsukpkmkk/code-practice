//
// Created by dandan on 2026/4/3.
//


#include <iostream>
#include <vector>

using namespace std;
int main() {
    vector<int> a;
    a.resize(10);
    for (int i : a) {
        cout<<i<<endl;
    }
    return 0;
}