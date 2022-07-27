#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1436번 - 영화감독 숌

int main() {

	int t, k, n, j;
	for (int i = 0; i <= 14; j++) {
		num[0][i] = i;
	}
	for (int a = 1; a <= 14; a++) {
		for (int b = 0; b <= 14; b++) {
			int sum = 0;
			for (int c = 0; c <= b; c++) {
				sum += num[a - 1][c];
			}
			num[a][b] = sum;
		}
	}
	/*
	scanf("%d", &t);

	for (j = 0; j < t; j++) {
		scanf("%d", &k);
		scanf("%d", &n);
		int cnt = 0;
		int num[15][15] = { 0 };
		
	}
	*/

	for (i = 0; i < 15; i++) {
		for (j = 0; j < 15; j++) {
			printf("[%d]", num[i][j]);
		}
		printf("[%d]\n");
	}
	

}