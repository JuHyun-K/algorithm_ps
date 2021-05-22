#include <iostream>
#define MAX 9
using namespace std;

int arr[MAX];
bool flag[MAX] = { 0, };
int n, m;

void solve(int depth) {
	if (depth == m) { // �������������� ���� ���
		for (int i = 0; i < m; i++)
			cout << arr[i] << ' ';
		cout << '\n';
		return;
	}

	for (int i = 1; i <= n; i++) {
		if (flag[i])
			continue;

		flag[i] = true; //Ž���� ��
		arr[depth] = i;// ���� �� ���
		solve(depth + 1); //��ͷ� ���� depth
		flag[i] = false; //���� i�� ������ ���� 

	}
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	cin >> n >> m;
	solve(0);
	
	system("pause");
}
