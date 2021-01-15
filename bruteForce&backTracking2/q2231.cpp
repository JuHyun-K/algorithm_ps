#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;



int main() {
	int i, j, n, tmp, sum = 0, ans = 0;
	vector<int> v;

	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	cin >> n;

	for (i = 1; i <= n; i++) {
		tmp = i; //나눌 수
		sum = i;
		while (tmp != 0) { // 자리수별로 끊기
			v.push_back(tmp % 10);
			tmp = tmp/10;
		}
	
		for (j = 0; j < v.size(); j++)
			sum += v[j];

		if (sum == n) {
			ans = i;
			break;
		}
			

		v.clear();
	}

	cout << ans <<endl;
	system("pause");
	return 0;
}
