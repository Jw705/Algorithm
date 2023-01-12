#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 2441번 - 별찍기 4

int main() {

	int n;
	scanf("%d", &n);
	int i, j;
	int m = n;

	for (i = 0; i < n; i++) {
		for (j = n; j > m; j--) {
			printf(" ");
		}
		for (j = 0; j < m; j++) {
			printf("*");
		}
		m--;
		printf("\n");
	}

}