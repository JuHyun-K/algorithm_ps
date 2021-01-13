#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	int i, n, score, maxSum = 0;
	vector<int> v;

	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	//input
	cin >> n;
	n = n * 2;
	for (i = 0; i < n; i++) {
		cin >> score;
		v.push_back(score);
	}

	//Ã³¸®
	sort(v.begin(), v.end());
	maxSum = 10000000;
	for (i = 0; i < n; i++) {
		maxSum = min(maxSum, (v[i] + v[n - i - 1]));
	}

	cout <<maxSum;
	system("pause");
	return 0;
}