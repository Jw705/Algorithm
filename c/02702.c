#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 2702번 - 초6수학

int gcd(int min, int max) {		// 최대공약수 구하기
	int remainder = 1;
	while (remainder) {
		remainder = max % min;
		max = min;
		min = remainder;
	}
	return max;
}

int lcm(int min, int max) {		// 최소공배수 구하기
	return min * max / gcd(min, max);
}

int main() {

	int t, a, b, min, max;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d %d", &a, &b);
		if (a > b) {
			max = a;
			min = b;
		}
		else {
			max = b;
			min = a;
		}
		printf("%d %d\n", lcm(min, max), gcd(min, max));
	}
}