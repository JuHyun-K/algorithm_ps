#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, maxHeight, height, ans, tmp;

int main() {

	int i, j;
	vector<int> v;

	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	//input
	cin >> n;

	for (i = 0; i < n; i++) {
		cin >> height;
		v.push_back(height);
	}

	//Ã³¸®
	height = 0;
	for (i = 0; i < n; i++) {
		if (v[i] >= maxHeight) {
			maxHeight = v[i];
			ans = max(ans, height);
			height = 0;
		}
		else
		{
			height++;
		}

	}

	ans = max(ans, height);

	cout <<ans;
	
	system("pause");

	return 0;
}
