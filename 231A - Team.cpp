#include <iostream>
using namespace std;
int main()
{
    int n, p, v, t, x = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> p >> v >> t;
        if (p + v + t >= 2)
        {
            x += 1;
        }
    }
    cout << x << endl;
}
