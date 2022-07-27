#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 2445¹ø - º°Âï±â 8

int main() {

	int n;
	scanf("%d", &n);
	int i, j;
	int m = n;

	for (i = 1; i <= n-1; i++) {
		for (j = 0; j < i; j++) {
			printf(" ");
		}
		for (j = 0; j < 2 * n - 2 * i; j++) {
			printf("*");
		}
		for (j = 0; j < i; j++) {
			printf(" ");
		}
		printf("\n");
	}
	for (i = n; i > 0; i--) {
		for (j = 0; j < i; j++) {
			printf("*");
		}
		for (j = 0; j < 2 * n - 2 * i; j++) {
			printf(" ");
		}
		for (j = 0; j < i; j++) {
			printf("*");
		}
		printf("\n");
	}
}