#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	int i, n, m, a, breadCount = 0;
	vector<int> v_10;
	vector<int> v_not10;

	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	//input
	cin >> n >> m;

	for (i = 0; i < n; i++) {
		cin >> a;
		if (a % 10 == 0)
			v_10.push_back(a);
		else
			v_not10.push_back(a);
	}

	//Ã³¸®
	sort(v_10.begin(), v_10.end());

	for (i = 0; i < v_10.size(); i++) {
		if (m <= 0)
			break;

		while (v_10[i] > 10 && m > 0) {
			v_10[i] -= 10;
			breadCount++;
			m--;
		}

		if (v_10[i] == 10) {
			breadCount++;
			continue;
		}		
	}
	
	for (i = 0; i < v_not10.size(); i++) {

		if (m <= 0)
			break;

		while (v_not10[i] > 10 && m > 0) {
				v_not10[i] -= 10;
				breadCount++;
				m--;
		}
	}

	cout << breadCount;

	system("pause");

	return 0;
}