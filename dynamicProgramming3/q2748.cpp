#include <iostream>
#include <algorithm>
#define MAX 100
using namespace std;

int n;
long long arr[MAX]; //long long���� �ؾ��� -> 90�� ������ ��ûĿ���Ƿ�

long long fibo(int num) {
	if (arr[num] != -1) //�̹� arr�� ��ϵǾ������Ƿ�
		return arr[num];

	if (num < 2) //2���� ������ ���� ���� �� x
		return arr[num] = num;

	return arr[num] = fibo(num-1) + fibo(num-2);
}


int main() {
	for (int i = 0; i < MAX; i++)
		arr[i] = -1;

	cin >> n;
	cout << fibo(n);
	system("pause");
}