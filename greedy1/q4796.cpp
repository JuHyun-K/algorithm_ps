#include <iostream>
#include <algorithm>

using namespace std;



int main() {
	int count = 0, L, P, V, i = 1;

	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	while (true) {
		cin >> L >> P >> V;
		
		if (L + P + V == 0)
			break;

		count = count + (V / P)*L + V % P;
		
		cout << "Case " << i++ << ": " << count << endl;
		count = 0;
	}


	return 0;
}