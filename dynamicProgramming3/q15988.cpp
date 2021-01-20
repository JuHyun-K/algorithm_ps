#include <iostream>
#include <algorithm>
#define MAX 10000000
using namespace std;

int t;
int nArr[MAX];
long long arr[MAX];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> t;
	for (int i = 0; i < t; i++)
		cin >> nArr[i];

	arr[1] = 1; arr[2] = 2; arr[3] = 4;

	for (int i = 0; i < t; i++) {
		for (int j = 4; j <= nArr[i]; j++) {
			if (arr[j] != 0) //값이 있는 건 넘어가도록
				continue;
			arr[j] = (arr[j - 1] + arr[j - 2] + arr[j - 3]) % 1000000009;
		}
		cout << arr[nArr[i]] << endl;
	}

	system("pause");
}