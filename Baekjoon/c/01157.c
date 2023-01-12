#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 1157번 - 단어 공부

int main() {

	char S[1000001];	
	int cf[123] = { 0 };
	scanf("%s", &S);

	int i = 0;
	while (S[i] != '\0') {
		if (S[i]>=97) cf[S[i]-32]++;
		else cf[S[i]]++;
		i++;
	}

	int maxj = 0;
	int max = 0;

	for (int j = 65; j <= 90; j++) {
		if (cf[j] > max) {
			max = cf[j];
			maxj = j;
		}
		else if (cf[j] == max) {
			maxj = 100;
		}
	}
	if (maxj == 100) printf("?");
	else printf("%c", maxj);

}