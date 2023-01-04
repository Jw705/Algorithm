#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1546번 - 평균

int main() {	

	int n = 0;
	scanf("%d", &n);

	double num[1000] = { 0 };
	double max = 0, sum = 0;

	for (int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
		if (max < num[i])max = num[i];
	}
	for (int i = 0; i < n; i++) {
		sum += num[i] / max * 100;
	}
		
	printf("%.6f\n", sum / n);
}