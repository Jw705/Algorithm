#include <stdio.h>
// [baekjoon] 21567번 - 숫자의 개수 2

int main() {

	long long A, B, C;
	long long D = 1;
	int cnt[10] = { 0 };
	scanf("%lld", &A);
	scanf("%lld", &B);
	scanf("%lld", &C);
	D = A * B * C;

	while (D > 0) {
		int n = D % 10;
		cnt[n]++;
		D /= 10;
	}

	for (int i = 0; i < 10; i++) {
		printf("%d\n", cnt[i]);
	}

}