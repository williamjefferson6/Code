#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s, c;
    cin >> s;
    for (int i = 0; i < s.length(); i++){
        if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U' || s[i] == 'Y' || s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'y'){
            continue;
        }
        c += '.';
        c += s[i];
    }
    transform(c.begin(), c.end(), c.begin(), ::tolower);
    cout << c;
}