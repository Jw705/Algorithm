#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 14582번 - 오늘도 졌다

int main() {

	int w[9], s[9], i;
	for (i = 0; i < 9; i++) {
		scanf("%d", &w[i]);
	}
	for (i = 0; i < 9; i++) {
		scanf("%d", &s[i]);
	}

	int is_wwinbefore = 0;
	int w_score = 0;
	int s_score = 0;

	for (i = 0; i < 9; i++) {
		w_score += w[i];
		if (w_score > s_score) is_wwinbefore = 1;
		s_score += s[i];
	}

	if (w_score < s_score && is_wwinbefore == 1) printf("Yes");
	else printf("No");

}