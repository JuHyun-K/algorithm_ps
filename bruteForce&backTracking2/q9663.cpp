//https://www.acmicpc.net/problem/9663
//https://stack07142.tistory.com/34
#include <iostream>
#include <math.h>
#define MAX 16 
using namespace std;

int n, ans = 0;
int board[MAX] = { -1, };

bool check(int r, int c) { //체크
	if (r < 1)
		return true;

	for (int row = 0; row < r; row++) { //같은열인지 || 대각선에 위치하는지
		if(board[row] == c || r - row == abs(c - board[row] ))
			return false;
	}
	return true;
}

void solve(int level) {
	int i;
	if (level == n) {
		ans++;
		return;
	}

	for (i = 0; i < n; i++) {
		if (check(level, i)) {
			board[level] = i;
			solve(level + 1);
			board[level] = -1;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	cin >> n;
	solve(0);
	cout << ans;
	system("pause");
}