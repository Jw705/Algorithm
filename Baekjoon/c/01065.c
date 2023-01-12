#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1065번 - 한수

int hansu(int n) {
	int arr[4] = { 0 };
	int i = 0;
	while (n > 0) {			// 입력받은 숫자의 각 자리수를 배열에 대입
		arr[i] = n % 10;
		n /= 10;
		i++;
	}

	switch (i) {
	case 1: case 2:	// 2자리수 이하일때는 무조건 한수
		return 1;	// 한수이면 1 반환
	case 3:			// 3자리수 일때 한수여부 판단
		if (arr[1] - arr[0] == arr[2] - arr[1]) return 1;	// 각 자리수의 차가 같으면 1 반환 (한수)
		else return 0;										// 같지 않으면 0 반환 (한수x)
	default:		// 4자리수 (=1000)일때는 한수가 아님
		return 0;	// 한수가 아니면 1 반환
	}
}

int main() {	

	int n, sum = 0;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		sum += hansu(i);
	}

	printf("%d\n", sum);
	
}