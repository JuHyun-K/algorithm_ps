#include <iostream>
#include <algorithm>
#define MAX 55

using namespace std;

char v[MAX][MAX];

int main() {
	int n, m;
	int i, j, l, k, count = 1e9;
	int n1, n2;

	cin >> n >> m;
	//�Է�
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			cin >> v[i][j];
		}
	}
	//ó��
	for (i = 0; i <= n-8; i++) { 
		//�־��� n���� �ּ� 8ĭ�� �ʿ��ϹǷ�, n-8���� ������ Ž��
		for (j = 0; j <= m-8; j++) {
		//���� i�� ����
			n1 = 0; //�� �� ĭ�� ����� ��, ����� ¦�� �������� Ȧ������
			n2 = 0; //�� ��ĭ�� ������, �������� Ȧ�� ����� ¦������
			for (k = i; k < i + 8; k++) {
				for (l = j; l < j + 8; l++) {
					if (v[k][l] == 'W') { //���ĭ �� ��
						if ((k + l) % 2 == 0) //Ȧ�������ϴµ�, ¦���̹Ƿ� n1++
							n1++;
						else// ¦������ �ϴµ�, Ȧ���̹Ƿ� n2++
							n2++;
					}
					else {//������ĭ�� ��
						if ((k + l) % 2 == 0)//¦��ĭ�� �ƴϸ� n2++
							n2++;
						else
							n1++;
					}
				}
			}
			count = min({ count, n1, n2 });
		}
	}
		
	cout << count;

	system("pause");
	return 0;
}