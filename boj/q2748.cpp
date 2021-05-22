#include <iostream>
#include <algorithm>
#define MAX 100
using namespace std;

int n;
long long arr[MAX]; //long long으로 해야함 -> 90을 넣으면 엄청커지므로

long long fibo(int num) {
	if (arr[num] != -1) //이미 arr에 기록되어있으므로
		return arr[num];

	if (num < 2) //2보다 작으면 값을 구할 수 x
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