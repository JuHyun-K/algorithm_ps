#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int d[10002];
int arr[10002][502][2];
//arr[a][b][c] : a���� i�п� �޸� �Ÿ�, b���� ��ħ����, c���� �ٴ��� ������
//arr[a][b][1]�� i�п� b�� ��ħ������ ������ �� �� �޸� �Ÿ��� �ִ밪 
//arr[a][b][0]�� i�п� b�� ��ħ������ ������ ���� ����
	//-> ���⼭ �� �� ���� �����ϸ� ��ħ������ 0�� �Ǿ�� �Ѵٴ� ����� �����ؾ�
//arr[a-1][b+1][0] : ���� �� ��츦 ���ϴµ�, ���� ����� �� ���� 

int main() { 
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int a, b;

	cin >> n >> m;
	for (a = 1; a <= n; a++)
		cin >> d[a];


	for (a = 1; a <= n; a++) {
		for (b = 0; b <= m; b++) { //��ħ������ m�� ������ �޸� �� x
			if (b != 1) {
				if (b != 0) {
					//��ħ����(b)�� 0�̳� 1�� �ƴ� �� 
					arr[a][b][1] = arr[a - 1][b-1][1] + d[a]; //������ �̾ �޸��� ���
					arr[a][b][0] = max(arr[a - 1][b + 1][1], arr[a - 1][b + 1][0]); //������ �޸��ٰ� �� ��
									//arr[a-1][b+1][] : �̹����� ���Ƿ�, ���� ���(a-1)�� b���� ��ħ������ ũ�Ƿ� b+1
				}
				else {//b�� 0�� == �̹����� ���ٴ� ��
					//���� ����� �����ų�, ���� ����� �޸� ���, ���� ����� 0�϶� ������ �� ���� ���
					arr[a][b][0] = max({ arr[a - 1][b + 1][0], arr[a - 1][b + 1][1], arr[a - 1][b][0] });
				}
			}
			else {
				//b == 1 -> �޸� ���� �ְ�, �� ���� ���� 
				//���ٰ� �޸��� ���� ���� ���
				arr[a][b][1] = max(arr[a - 1][b - 1][1], arr[a - 1][b - 1][0]) + d[a];
				//��� ���� ���
				arr[a][b][0] = max(arr[a - 1][b + 1][1], arr[a - 1][b + 1][0]);
			}
			
		}
	}

	cout << arr[n][0][0]; //n�ʿ���, ��ħ������ 0�� ���� + �ȴ޸��� ����(���� ���ǿ� ����)
	system("pause");
}