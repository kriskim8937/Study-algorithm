#include <iostream>
#include <string.h>
using namespace std;
void calc(char *a);
char b[111]; //문자열 입력받고 매겨변수 전달받는법
int x;
int s=0;
int n=20;
int main()
{
	int m;
	scanf("%d", &m);
	while (m--)
	{
		scanf("%s", b);
		calc(b);
	}
	return 0;
}
void calc(char *a)
{
	if (!strcmp(a, "add"))//문자열 비교 string compare
	{
		scanf("%d", &x);
		x--;
		s = (s | (1 << x));
	}
	else if (!strcmp(a, "remove"))
	{
		scanf("%d", &x);
		x--;
		s = (s & ~(1 << x));
	}
	else if (!strcmp(a, "check"))
	{
		scanf("%d", &x);
		x--;
		int res = (s & (1 << x));
		if (res)
		{
			printf("1\n");
		}
		else
		{
			printf("0\n");
		}
	}
	else if (!strcmp(a, "toggle"))
	{
		scanf("%d", &x);
		x--;
		s = (s ^ (1 << x));//not연산으로 0을1로, 1을 0으로
	}
	else if (!strcmp(a, "all"))
	{
		s = (1 << n) - 1;//20만금 비트쉬프트 한수 1을빼면 전부 11111
	}
	else if (!strcmp(a, "empty"))
	{
		s = 0;
	}
	return;
}
//ctrl+alt+c == compiling
//ctrl+alt+r == execute
//cirl+k+f == align
//cirl+/ == 주석처리
//cirl+H == 변수 변경
//1억이 1초로
