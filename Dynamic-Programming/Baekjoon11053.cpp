
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	scanf("%d", &n);
	vector<int> a(n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}
	vector<int> d(n);
	for (int i = 0; i < n; i++)
	{
		d[i] = 1;
		for (int j = 0; j < i; j++)
		{
			if (a[i] > a[j] && d[i] < d[j] + 1)
			{
				d[i] = d[j] + 1;
				
			}
		}
	}
	/*for (int i = 0; i < n; i++)
	{
		printf("%d, ", d[i]);
	}*/
	printf("%d", *max_element(d.begin(), d.end()));

}
