//https://www.acmicpc.net/board/view/19169
#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[1000002]; //10^6 ���϶�� �����Ƿ� +1, +2���� ���ִ°� ����

/* 0�� ��� ó���ؾ��� �� ���� 30��° �ٺ��� ������ �� ��
int main1() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;
	int tmp, x = 0, y = 0, z = 0;

	arr[1] = 0; arr[2] = 1; arr[3] = 1;

	for (int i = 4; i <= n; i++) {
		tmp = i; x = 0; y = 0; z = 0;

		if (tmp % 2 == 0) //2�ǹ��
			x = tmp / 2;
		if (tmp % 3 == 0) //3�ǹ��
			y = tmp / 3;
		
		z = tmp - 1; //��� ��쿡 ����ؼ�

		if (arr[x] == 0 && arr[y] == 0) //�Ҽ�
			arr[i] = arr[z] + 1;
		else if (arr[x] == 0 && arr[y] != 0)//2�� ���x, 3�ǹ��o
			arr[i] = min(arr[y], arr[z]) + 1;
		else if (arr[x] != 0 && arr[y] == 0)//2�ǹ��o, 3�ǹ��x
			arr[i] = min(arr[x], arr[z]) + 1;
		else if(arr[x] != 0 && arr[y] != 0) //6�� ���
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
		arr[i] = arr[i - 1] + 1; //��� ��쿡 ����ؼ�, ���� ������ ������ +1

		//3�� ����� ��, 3���� ���� �ε����� ��
		if (tmp % 3 == 0) //3�ǹ��
			arr[i] = min(arr[tmp], arr[tmp/3]+1);

		//2�� ����� ��, 2���� ���� �ε����� ��(�ڵ����� 3��i�� ���� ������ �� ���� ���� �񱳵�)
		if (tmp % 2 == 0) //2�ǹ��
			arr[i] = min(arr[tmp], arr[tmp / 2] + 1);
	}

	cout << arr[n];
	system("pause");
}