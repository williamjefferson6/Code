#include <iostream> 
using namespace std;
int main()
{
    int n, k;
    cin >> n >> k;
    int x;
    for (int i = 0; i < k; i++){
        cin >> x;
        if (x == 0){
            cout << i << endl;
            return 0;
        }
    }
    int y;
    for (int i = k; i < n; i++){
        cin >> y;
        if (y != x){
            cout << i << endl;
            return 0;
        }
    }
    cout << n <<endl;
    return 0;
}
