#include <iostream>
using namespace std;

int main() {
	int month, date, count = 0;
	int month_date[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	scanf_s("%d %d", &month, &date);
	for (int i = 1; i < month; i++)
	{
		count += month_date[i-1];
	}
	
	int a = 0;
	a = count + date;
	a = a % 7;
	if (a == 1)
	{
		printf("MON");
	}
	else if (a == 2)
	{
		printf("TUE");
	}
	else if (a == 3)
	{
		printf("WED");
	}
	else if (a == 4)
	{
		printf("THU");
	}
	else if (a == 5)
	{
		printf("FRI");
	}
	else if (a == 6)
	{
		printf("SAT");
	}
	else if (a == 0)
	{
		printf("SUN");
	}

	//printf("\n\n%d", a);
	/* 
		달력 출력
	*/
	

	return 0;

}
