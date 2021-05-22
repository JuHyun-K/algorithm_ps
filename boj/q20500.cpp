#include <iostream>
#include <algorithm>

using namespace std;

int n;
long long dp[1516][3];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int i, j, case1, case5;
	cin >> n;

	dp[1][2] = 1;
	dp[2][0] = 1; dp[2][1] = 1;

	for (i = 3; i <= n; i++) {
		dp[i][0] = (dp[i - 1][1] + dp[i - 1][2])% 1000000007;
		dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 1000000007;
		dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 1000000007;
	}


	cout << dp[n][0];
	system("pause");
}
