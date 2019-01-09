
#include <iostream>
#include <algorithm>  
#include <vector>

using namespace std;

int main() {

	int n;

	scanf("%d", &n);

	vector<int> a(n + 1);

	for (int i = 1; i <= n; i++) {

		scanf("%d", &a[i]);

	}

	vector<int> d(n + 1);

	for (int i = 1; i <= n; i++) {

		for (int j = 1; j <= i; j++) {

			d[i] = max(d[i], d[i - j] + a[j]);

		}

	}

	printf("%d\n", d[n]);
	

	return 0;

}
/*
*/
