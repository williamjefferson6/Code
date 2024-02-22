#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int t, k = 0, n, c = 0, temp = 0;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
			int x = n;
			while (x != 0) {
				if (x % 10 != 0) {
					k++;
				}
				x = x / 10;
			}
			cout << k << endl;
			while (n != 0) {
				temp = n % 10 * pow(10, c);
				if (temp != 0) {
					cout << temp << " ";
				}
				n = n / 10;
				c++;
			}
			cout << endl;
			k = 0;
			c = 0;
	}
}