#include <stdio.h>
// [baekjoon] 2609번 - 최대공약수와 최소공배수

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

	int a, b, min, max;
	scanf("%d %d", &a, &b);
	if (a > b) {
		max = a;
		min = b;
	}
	else {
		max = b;
		min = a;
	}
	printf("%d\n%d", gcd(min, max), lcm(min, max));
}