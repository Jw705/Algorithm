#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1475번 - 방번호

int main() {

	int s[10] = { 0 };
	int n;

	scanf("%d", &n);

	if (n == 0) {
		printf("1");
		return 0;
	}
	while (n > 0) {
		if (n % 10 == 6 && s[6] > s[9]) s[9]++;
		else if (n % 10 == 9 && s[9] > s[6]) s[6]++;
		else s[n % 10]++;
		n /= 10;		
	}

	int max = 0;
	for (int i = 0; i < 10; i++) {
		if (s[i] > max) max = s[i];
	}
	printf("%d ", max);

}