#include <stdio.h>
// [baekjoon] 4673번 - 셀프 넘버

int d(int n) {
	int sum = n;
	while (n > 0) {
		sum += n % 10;
		n /= 10;
	}
	return sum;
}

int main() {		
	int num[10001] = { 0 };

	for (int i = 1; i <= 10000; i++) {
		if (d(i) <= 10000) num[d(i)] = -1;
	}
	for (int i = 1; i <= 10000; i++) {
		if (num[i] != -1) printf("%d\n", i);
	}
}