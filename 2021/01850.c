#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1850번 - 최대공약수

long long gcd(long long min, long long max) {
	long long remainder = 1;
	while (remainder) {
		remainder = max % min;
		max = min;
		min = remainder;
	}
	return max;
}

int main() {

	long long a, b, i, min, max;
	scanf("%lld %lld", &a, &b);

	if (a > b) {
		max = a;
		min = b;
	}
	else {
		max = b;
		min = a;
	}
	for (i = 0; i < gcd(min, max); i++)	printf("1");

}