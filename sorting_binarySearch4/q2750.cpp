#include <iostream>
#include <algorithm>


using namespace std;

int v[10002];
int n;

//i는 pivot보다 큰 값까지 이동하다 중단
//j는 pivot보다 작은 값까지 이동하다 중단

int partition(int left, int right) {

	int tmp, low, high, pivot;
	low = left + 1;
	high = right;
	pivot = v[left];

	while (low < high) {//나눈 v의 크기가 0 or 1이 될 때까지 반복
		while (low <= right && v[low] < pivot) {
			low++;//i가 end보다 작고, v[i]가 pivot값보다 작으면 그 다음 값을 가리킴(왼->오)
		}
		while (high >= left && v[high] > pivot) {//(오->왼)
			high--;
		}
		if (low < high) {
			tmp = v[low];
			v[low] = v[high];
			v[high] = tmp;
		}
	}
	//피벗을 가운데로
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

	quickSort(0, n-1); //index값을 주는 거니까 n-1
	cout << endl;
	for (i = 0; i < n; i++)
		cout << v[i] << endl;

	system("pause");
}