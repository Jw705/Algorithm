#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 10992번 - 별찍기

int main() {

	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	int all_suip = 0;
	int all_biyong = a;
	int i = 0;

	while (all_suip < all_biyong) {
		all_suip += c;
		all_biyong += b;
		i++;
	}
	
	printf("%d",i);



}