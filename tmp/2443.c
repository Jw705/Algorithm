#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 2443¹ø - º°Âï±â 6

int main() {

	int n;
	scanf("%d", &n);
	int i, j;
	int m = n;

	for (i = 1; i <= n; i++) {
		for (j = 0; j < i-1; j++) {
			printf(" ");
		}
		for (j = 0; j < 2 * n - (2*i-1); j++) {
			printf("*");
		}
		printf("\n");
	}

}