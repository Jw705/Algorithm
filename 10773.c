#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 10773 - 제로

int main() {

	int k,j;

	scanf("%d", &k);
	
	int num[100000] = { 0 };

	long long sum = 0;
	int i = 0;
	
	for (j = 0; j < k; j++) {
		int n;
		scanf("%d", &n);
		if (n == 0) {
			i--;
			*(num + i) = 0;
		}
		else {
			*(num + i) = n;
			i++;
		}
	}
	for (i = 0; i < k; i++) {
		sum += *(num + i);
	}

	printf("%lld", sum);

}