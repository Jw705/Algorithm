#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1065�� - �Ѽ�

int hansu(int n) {
	int arr[4] = { 0 };
	int i = 0;
	while (n > 0) {			// �Է¹��� ������ �� �ڸ����� �迭�� ����
		arr[i] = n % 10;
		n /= 10;
		i++;
	}

	switch (i) {
	case 1: case 2:	// 2�ڸ��� �����϶��� ������ �Ѽ�
		return 1;	// �Ѽ��̸� 1 ��ȯ
	case 3:			// 3�ڸ��� �϶� �Ѽ����� �Ǵ�
		if (arr[1] - arr[0] == arr[2] - arr[1]) return 1;	// �� �ڸ����� ���� ������ 1 ��ȯ (�Ѽ�)
		else return 0;										// ���� ������ 0 ��ȯ (�Ѽ�x)
	default:		// 4�ڸ��� (=1000)�϶��� �Ѽ��� �ƴ�
		return 0;	// �Ѽ��� �ƴϸ� 1 ��ȯ
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