#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 21867¹ø - Java Bitecode

int main() {

	int N;
	char S[200000];				
	scanf("%d", &N);
	scanf("%s", &S);
	int b_len = 0;

	for (int i = 0; i < N; i++) {
		if (S[i] != 'J'&&S[i] != 'A'&&S[i] != 'V') {
			printf("%c", S[i]);
			b_len++;
		}
	}
	if (b_len ==0) printf("nojava");

}