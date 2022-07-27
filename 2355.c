#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 2355¹ø - º°Âï±â 12

int main() {

	int n;
	scanf("%d", &n);
	int i, j;
	int m = n;

	for (i = 1; i <= n - 1; i++) {

		for (j = 0; j < i; j++) {
			printf("*");
		}
		printf("\n");
	}

	for (i = n; i > 0; i--) {

		for (j = 0; j < i; j++) {
			printf("*");
		}
		printf("\n");
	}

}