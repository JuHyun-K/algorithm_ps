//https://www.acmicpc.net/board/view/19169
#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[1000002]; //10^6 이하라고 했으므로 +1, +2정도 해주는게 맞음

/* 0을 어떻게 처리해야할 지 몰라서 30번째 줄부터 엉뚱한 짓 함
int main1() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;
	int tmp, x = 0, y = 0, z = 0;

	arr[1] = 0; arr[2] = 1; arr[3] = 1;

	for (int i = 4; i <= n; i++) {
		tmp = i; x = 0; y = 0; z = 0;

		if (tmp % 2 == 0) //2의배수
			x = tmp / 2;
		if (tmp % 3 == 0) //3의배수
			y = tmp / 3;
		
		z = tmp - 1; //모든 경우에 대비해서

		if (arr[x] == 0 && arr[y] == 0) //소수
			arr[i] = arr[z] + 1;
		else if (arr[x] == 0 && arr[y] != 0)//2의 배수x, 3의배수o
			arr[i] = min(arr[y], arr[z]) + 1;
		else if (arr[x] != 0 && arr[y] == 0)//2의배수o, 3의배수x
			arr[i] = min(arr[x], arr[z]) + 1;
		else if(arr[x] != 0 && arr[y] != 0) //6의 배수
			arr[i] = min({ arr[x], arr[y], arr[z] }) + 1;
			
	}
	
	cout << arr[n] <<endl;
	system("pause");
}
*/

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;
	int tmp;

	arr[1] = 0;
	for (int i = 2; i <= n; i++) {
		tmp = i;
		arr[i] = arr[i - 1] + 1; //모든 경우에 대비해서, 이전 값보다 무조건 +1

		//3의 배수일 때, 3으로 나눈 인덱스와 비교
		if (tmp % 3 == 0) //3의배수
			arr[i] = min(arr[tmp], arr[tmp/3]+1);

		//2의 배수일 때, 2으로 나눈 인덱스와 비교(자동으로 3과i를 비교한 값에서 더 작은 값이 비교됨)
		if (tmp % 2 == 0) //2의배수
			arr[i] = min(arr[tmp], arr[tmp / 2] + 1);
	}

	cout << arr[n];
	system("pause");
}