#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	int i, n, time1, time2, start, count = 0;
	vector<pair<int, int>> v;

	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	//input
	cin >> n;

	for (i = 0; i < n; i++) {
		cin >> time1 >> time2;
		v.push_back({time2, time1});
	}

	//처리
	sort(v.begin(), v.end()); //벡터의 앞 자료 기준으로 오름차순 정렬해줌
	
	start = -1;

	for (i = 0; i < n; i++) {
		if (v[i].second < start)
			continue;
		
		start = v[i].first;
		count++;
	}

	cout << count;
	system("pause");
	return 0;
}