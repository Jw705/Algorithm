#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 11557�� - Yangjojang of The Year

int main() {

	int T, N, L[100];
	char S[100][21];					// �б� �̸��� ������ 2���� �迭!
	scanf("%d", &T);			

	for (int i = 0; i < T; i++) {
		scanf("%d", &N);
		int max_num = 0;				// �� �Һ� ���� ���� �б��� ����
		int max_sul = 0;				// �� �Һ� ���� ���� �б��� �� �Һ�
		
		for (int j = 0; j < N; j++) {
			scanf("%s%d", &S[j], &L[j]);
			if (L[j] > max_sul) {		// �� �Һ� ��
				max_sul = L[j];
				max_num = j;
			}
		}
		printf("%s\n", S[max_num]);
	}

}