#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 9012번 - 괄호

int main() {

	int t,i,j;
	char s[60];

	scanf("%d", &t);

	for (i = 0; i < t; i++) {
		scanf("%s", &s);
		int cnt1 = 0;
		int cnt2 = 0;
		for (j = 0; j < strlen(s); j++) {
			if (s[j] == '(')cnt1++;
			else if (s[j] == ')')cnt2++;
			if (cnt1 < cnt2) cnt2 = 100;
		}
		if (cnt1 == cnt2 && s[j - 1] == ')') printf("YES\n");
		else printf("NO\n");
	}
	
}