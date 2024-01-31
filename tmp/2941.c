#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 2941번 - 크로아티아 알파벳

int main() {

	char s[105];

	scanf("%s", &s);
	
	int cnt = strlen(s);

	for (int i = 1; i < strlen(s); i++) {
		if (i > 1 && s[i - 2] == 'd'&&s[i - 1] == 'z'&&s[i] == '=') cnt -= 2;
		else if (s[i - 1] == 'c'&&s[i] == '=') cnt--;
		else if (s[i - 1] == 'c'&&s[i] == '-') cnt--;
		else if (s[i - 1] == 'd'&&s[i] == '-') cnt--;
		else if (s[i - 1] == 'l'&&s[i] == 'j') cnt--;
		else if (s[i - 1] == 'n'&&s[i] == 'j') cnt--;
		else if (s[i - 1] == 's'&&s[i] == '=') cnt--;
		else if (s[i - 1] == 'z'&&s[i] == '=') cnt--;
	}

	printf("%d", cnt);

}
