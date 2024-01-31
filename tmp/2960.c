#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 2960번 - 에라토스테네스의 체

int main() {

	int num[1001] = { 1,1, 0 };

	int n, k;
	int cnt = 0;

	scanf("%d %d", &n, &k);


	for (int i = 2; i <= n; i++) {
		if (num[i] == 0) {
			for (int j = 1; i*j <= n; j++) {
				if (num[i*j] == 0) {
					num[i*j] = 1;
					cnt++;
					if (cnt == k) {
						printf("%d", i*j);
						break;
					}
				}			
				
			}
		}
	}

}
