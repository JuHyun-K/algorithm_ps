#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	int i, j, n, score, count = 0;
	vector<int> v;
	
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	//input
	cin >> n;

	for (i = 0; i < n; i++) {
		cin >> score;
		v.push_back(score);
	}

	//Ã³¸®

	for (i = n - 2; i >= 0; i--) {
		if (v[i + 1] <= v[i])
			count = v[i] - v[i + 1] + 1 + count;
		v[i] = min(v[i + 1] - 1, v[i]);
	}

	cout << count;
	system("pause");
	return 0;
}