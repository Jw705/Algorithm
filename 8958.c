#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 8958번 - OX퀴즈

int main() {	

	int arr[3000000];
	int n = 0;			
	scanf("%d", &n);	// 테스트 케이스 개수 입력
	getchar();			// 엔터 처리

	char ox[80];

	for (int i = 0; i < n; i++) {
		int cnt = 0, sum = 0;

		for (int j = 0; j < 80; j++) {
			scanf("%c", &ox[j]);
			if (ox[j] == 'O') {
				cnt++;
				sum += cnt;
			}
			else if (ox[j] == 'X') {
				cnt = 0;
			}
			else break;
		}

		printf("%d\n", sum);
	}		
	
}
