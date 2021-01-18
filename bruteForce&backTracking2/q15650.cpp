#include <iostream>
#define MAX 9
using namespace std;

int arr[MAX];
bool flag[MAX] = { 0, };
int n, m;

void solve(int depth, int num) {
	if (depth == m) { // 마지막레벨까지 왔을 경우
		for (int i = 0; i < m; i++)
			cout << arr[i] << ' ';
		cout << '\n';
		return;
	}

	for (int i = num; i <= n; i++) {
		if (flag[i])
			continue;

			flag[i] = true;
			arr[depth] = i;
			solve(depth + 1, i+1);
			flag[i] = false;
	}
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	cin >> n >> m;
	solve(0, 1);

	system("pause");
}
