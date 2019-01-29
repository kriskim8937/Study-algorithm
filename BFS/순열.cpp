//완전 탐색 순열 
#include <iostream>
#include <vector>
using namespace std;
int lon = 3;

void go(int index, int a[], int asize, vector<int> &pick, vector<bool> &visit)
{
	if(index == lon)
	{
		for(int i=0;i<pick.size();i++)
		{
			printf("%d ",pick[i]);
		}
		printf("\n");
		return;
	}
	for(int i=0; i<asize;i++)
	{
		if(!visit[i])
		{
			visit[i]=true;pick.push_back(a[i]);
			go(index+1,a, asize, pick, visit);
			visit[i]=false;pick.pop_back();
		}
	}
}
int main()
{
	int a[] = {6,3,2};
	int asize = sizeof(a)/sizeof(a[0]);
	vector<int> pick;
	vector<bool> visit(asize,false);
	go(0,a,asize,pick,visit);
	return 0;
}
