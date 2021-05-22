#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int d[10002];
int arr[10002][502][2];
//arr[a][b][c] : a에는 i분에 달릴 거리, b에는 지침지수, c에는 뛰는지 쉬는지
//arr[a][b][1]는 i분에 b의 지침지수를 가지고 뛸 때 달린 거리의 최대값 
//arr[a][b][0]는 i분에 b의 지침지수를 가지고 뛰지 않음
	//-> 여기서 한 번 쉬기 시작하면 지침지수가 0이 되어야 한다는 사실을 명심해야
//arr[a-1][b+1][0] : 내가 쉴 경우를 구하는데, 이전 사람이 쉰 상태 

int main() { 
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int a, b;

	cin >> n >> m;
	for (a = 1; a <= n; a++)
		cin >> d[a];


	for (a = 1; a <= n; a++) {
		for (b = 0; b <= m; b++) { //지침지수가 m을 넘으면 달릴 수 x
			if (b != 1) {
				if (b != 0) {
					//지침지수(b)가 0이나 1이 아닐 때 
					arr[a][b][1] = arr[a - 1][b-1][1] + d[a]; //이전에 이어서 달리는 경우
					arr[a][b][0] = max(arr[a - 1][b + 1][1], arr[a - 1][b + 1][0]); //이전에 달리다가 쉴 때
									//arr[a-1][b+1][] : 이번에는 쉬므로, 이전 사람(a-1)은 b보다 지침지수가 크므로 b+1
				}
				else {//b가 0임 == 이번에도 쉰다는 뜻
					//이전 사람이 쉬었거나, 이전 사람이 달린 경우, 이전 사람이 0일때 쉬었다 또 쉬는 경우
					arr[a][b][0] = max({ arr[a - 1][b + 1][0], arr[a - 1][b + 1][1], arr[a - 1][b][0] });
				}
			}
			else {
				//b == 1 -> 달릴 수도 있고, 쉴 수도 있음 
				//쉬다가 달리는 것을 택한 경우
				arr[a][b][1] = max(arr[a - 1][b - 1][1], arr[a - 1][b - 1][0]) + d[a];
				//계속 쉬는 경우
				arr[a][b][0] = max(arr[a - 1][b + 1][1], arr[a - 1][b + 1][0]);
			}
			
		}
	}

	cout << arr[n][0][0]; //n초에서, 지침지수가 0인 상태 + 안달리는 상태(문제 조건에 따라)
	system("pause");
}