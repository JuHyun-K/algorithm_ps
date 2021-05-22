#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	int i, n, count = 0;
	vector<int> v;

	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	cin >> n;

	//섞자, 5와 3을
	while (true) {
		//5의배수
		if (n % 5 == 0) {
			count += n / 5;
			break;
		}

		n -= 3;
		count++;

		if (n == 0)
			break;

		if (n < 0) {
			count = -1;
			break;
		}
	}
	cout << count;

	system("pause");
	return 0;
}