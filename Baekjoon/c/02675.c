#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 2675번 - 문자열 반복

int main() {	

	int n;
	scanf("%d", &n);
	int i, j;
	int m = n;

	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			printf("*");
		}
		m--;
		printf("\n");
	}

}