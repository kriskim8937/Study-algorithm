//주석 설정 단축키 : ctrl + K + C, 해제: ctrl + K + U
//백준 1546번 평균

// double,float형은 둘다 %f로 출력
// double,int형 섞어서 계산 가능 
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int N = 0;
double maxN,sum = 0.0;
int a[10001] = { 0, };
int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &a[i]);
		if (a[i] > maxN) {
			maxN = a[i];
		}
	}
	for (int i = 0; i < N; i++) {
		sum += ((a[i] / maxN) * 100);
	}
	printf("%.2f", sum/N);
}
