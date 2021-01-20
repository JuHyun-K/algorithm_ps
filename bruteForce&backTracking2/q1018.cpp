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
	//입력
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			cin >> v[i][j];
		}
	}
	//처리
	for (i = 0; i <= n-8; i++) { 
		//주어진 n에서 최소 8칸이 필요하므로, n-8범위 내에서 탐색
		for (j = 0; j <= m-8; j++) {
		//위의 i와 동일
			n1 = 0; //맨 윗 칸이 흰색일 때, 흰색은 짝수 검은색은 홀수여야
			n2 = 0; //맨 윗칸이 검은색, 검은색은 홀수 흰색은 짝수여야
			for (k = i; k < i + 8; k++) {
				for (l = j; l < j + 8; l++) {
					if (v[k][l] == 'W') { //흰색칸 일 때
						if ((k + l) % 2 == 0) //홀수여야하는데, 짝수이므로 n1++
							n1++;
						else// 짝수여야 하는데, 홀수이므로 n2++
							n2++;
					}
					else {//검은색칸일 때
						if ((k + l) % 2 == 0)//짝수칸이 아니면 n2++
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