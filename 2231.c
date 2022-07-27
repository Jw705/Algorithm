#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 2231번 - 분해합

int main() {

	int n, i;

	scanf("%d", &n);

	int m = 0;

	for (i = 1; i < n; i++) {
		int sum = i;
		int i2 = i;
		while (i2 > 0) {
			sum += i2 % 10;
			i2 /= 10;
		}
		if (sum == n) {
			printf("%d\n", i);
			break;
		}
	}
	if (i == n) {
		printf("0");
	}

}