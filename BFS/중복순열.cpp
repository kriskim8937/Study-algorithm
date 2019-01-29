//중복 순열이란 총길이가 n이고, 각각의 선택할 수 있는게 m개 있으면, 총 갯수가 m^n개 되는 순열이다.
#include <iostream>
#include <vector>
using namespace std;
int lon = 3;

void go(int index, vector<int> &pick, int a[], int asize)
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
		pick.push_back(a[i]);
		go(index+1,pick, a, asize);
		pick.pop_back();
	}
}
int main()
{
	int a[] = {6,3,2};
	int asize = sizeof(a)/sizeof(a[0]);
	vector<int> pick;
	go(0,pick,a,asize);
	return 0;
}
//ctrl+alt+c == compiling
//ctrl+alt+r == execute
//cirl+k+f == align
//cirl+/ == 주석처리
//cirl+H == 변수 변경
//1억이 1초로
