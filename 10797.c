#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 10991�� - �� ���-16

int main() {

	int n;
	scanf("%d", &n);

	for (i = 0; i <= n; i++) {

		for (j = 0; j < n-i; j++) {
			printf(" ");
		}
		printf("\n");

		printf("*");
	}


}