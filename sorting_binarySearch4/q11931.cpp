#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> v;

bool comp(int a, int b) { //Ä¿½ºÅÒ °¡´É
	return a > b;
}

int main() {
	int i, tmp;

	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> tmp;
		v.push_back(tmp);
	}

	sort(v.begin(), v.end(), comp);

	for (i = 0; i < n; i++)
		cout << v[i] <<'\n';

	system("pause");
}

/*
int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		int t;
		scanf("%d", &t);
		num[t + 1000000] = 1;
	}
	for (int i = 2000000; i >= 0; i--) {
		if (num[i] == 1)
			printf("%d\n", i - 1000000);
	}
}

*/