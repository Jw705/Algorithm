#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 10991�� - �� ���-16

int main() {

	int n,i,j;
	scanf("%d", &n);

	for (i = 1; i <= n; i++) {

		for (j = 0; j < n - i; j++) {
			printf(" ");
		}
		
		for (j = 0; j < i; j++) {
			printf("*");
			if (j == i);
			else printf(" ");
		}
		printf("\n");
	}


}