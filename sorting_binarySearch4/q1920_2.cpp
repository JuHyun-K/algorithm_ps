//https://www.acmicpc.net/board/view/25204

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m;
vector<int> v;

int binarySearch(int key) {//첫 번째 입력배열과 key값 비교
	int left = 0, right = n - 1, mid;

	while (left <= right) {
		mid = (left + right) / 2;
		if (key == v[mid]) return 1;

		if (key < v[mid]) right = mid - 1;
		else left = mid + 1;
	}
	return 0;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); 

	int i, tmp;
	//입력
	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> tmp;
		v.push_back(tmp);
	}

	//정렬
	sort(v.begin(), v.end());
	//두 번째 배열 처리
	cin >> m;
	for (i = 0; i < m; i++) {
		cin >> tmp;
		cout << binarySearch(tmp) <<'\n';
	}
	system("pause");
}