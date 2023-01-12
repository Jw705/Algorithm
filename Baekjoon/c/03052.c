#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 3052번 - 나머지

int main() {	

	int a, b, c;
	int num[1001] = { 0 };

	for (int i = 0; i < 10; i++) {
		scanf("%d", &a);
		num[a % 42] = 1;
	}

	int cnt = 0;
	for (int i = 0; i <= 1000; i++) {
		if (num[i] > 0) cnt++;
	}
	
	printf("%d\n", cnt);
}