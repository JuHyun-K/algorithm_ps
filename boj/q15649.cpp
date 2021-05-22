#include <iostream>
#define MAX 9
using namespace std;

int arr[MAX];
bool flag[MAX] = { 0, };
int n, m;

void solve(int depth) {
	if (depth == m) { // 마지막레벨까지 왔을 경우
		for (int i = 0; i < m; i++)
			cout << arr[i] << ' ';
		cout << '\n';
		return;
	}

	for (int i = 1; i <= n; i++) {
		if (flag[i])
			continue;

		flag[i] = true; //탐색한 것
		arr[depth] = i;// 현재 수 기록
		solve(depth + 1); //재귀로 다음 depth
		flag[i] = false; //현재 i는 다음을 위해 

	}
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	cin >> n >> m;
	solve(0);
	
	system("pause");
}
