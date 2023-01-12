#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] ﻿1759번 - 암호 만들기

void makepw(char *origin, char *tmp, int l, int c, int i, int k);
void prt(char *tmp, int c);

int main() {
	int l, c;
	scanf("%d %d", &l, &c);
	char ar[15] = { 0 };
	for (int i = 0; i < c; i++) {		// 알파벳 입력받기
		getchar();
		scanf("%c", &ar[i]);
	}

	for (int i = c - 1; i > 0; i--) {	// 입력받은 알파벳을 정렬
		for (int j = 0; j < i; j++) {
			if (ar[i] < ar[j]) {
				char tmpc = ar[i];
				ar[i] = ar[j];
				ar[j] = tmpc;
			}
		}
	}
	char tmp[16] = { 0 };
	makepw(ar, tmp, l, c, 0, 0);
	return 0;
}

void makepw(char *origin, char *tmp, int l, int c, int i, int k) {	// 암호로 사용했을 법한 문자 만들기
	if (i == l) prt(tmp, l);
	else {
		for (int k2 = k; k2 < c; k2++) {
			tmp[i] = origin[k2];
			mk(origin, tmp, l, c, i + 1, k2 + 1);
		}
	}
}

void prt(char *tmp, int c) {	// 최소 한 개의 모음과 두 개의 자음으로 구성되어 있는지 확인하고 출력
	int cnt_a = 0;
	int cnt_b = 0;
	for (int k = 0; k < c; k++) {
		if (tmp[k] == 'a' || tmp[k] == 'e' || tmp[k] == 'i' || tmp[k] == 'o' || tmp[k] == 'u') cnt_a++;
		else cnt_b++;
	}
	if (cnt_a >= 1 && cnt_b >= 2)printf("%s\n", tmp);
}