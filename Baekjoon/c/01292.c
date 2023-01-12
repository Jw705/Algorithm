#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1292번 - 저항

int main() {

	int s[2000] = { 0 };
	int a, b, j;

	scanf("%d %d", &a, &b);

	int i = 0;
	int n = 1;
	while (i < 1000) {
		for (j = 0; j < n; j++) {
			s[i] = n;
			i++;
		}
		n++;
	}

	int sum = 0;

	for (i = a - 1; i < b; i++) {
		sum += s[i];
	}
	printf("%d ", sum);
}