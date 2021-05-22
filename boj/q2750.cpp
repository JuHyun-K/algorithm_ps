#include <iostream>
#include <algorithm>


using namespace std;

int v[10002];
int n;

//i�� pivot���� ū ������ �̵��ϴ� �ߴ�
//j�� pivot���� ���� ������ �̵��ϴ� �ߴ�

int partition(int left, int right) {

	int tmp, low, high, pivot;
	low = left + 1;
	high = right;
	pivot = v[left];

	while (low < high) {//���� v�� ũ�Ⱑ 0 or 1�� �� ������ �ݺ�
		while (low <= right && v[low] < pivot) {
			low++;//i�� end���� �۰�, v[i]�� pivot������ ������ �� ���� ���� ����Ŵ(��->��)
		}
		while (high >= left && v[high] > pivot) {//(��->��)
			high--;
		}
		if (low < high) {
			tmp = v[low];
			v[low] = v[high];
			v[high] = tmp;
		}
	}
	//�ǹ��� �����
	if (v[left] > v[high]) {
		tmp = v[left];
		v[left] = v[high];
		v[high] = tmp;
	}
		
	
	return high;
}

void quickSort(int left, int right) {
	int pivot;

	if (left < right) {
		pivot = partition(left, right);
		quickSort(left, pivot - 1);
		quickSort(pivot + 1, right);
	}
}

int main() {
	int i, j, tmp;
	cin >> n;

	for (i = 0; i < n; i++)
		cin >> v[i];

	quickSort(0, n-1); //index���� �ִ� �Ŵϱ� n-1
	cout << endl;
	for (i = 0; i < n; i++)
		cout << v[i] << endl;

	system("pause");
}