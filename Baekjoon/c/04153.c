#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 4153번 - 직각삼각형

int main() {

	int a, b, c;

	int q = 0;
	while (q == 0) {
		scanf("%d %d %d", &a, &b, &c);
		if (a*b*c == 0) {
			q = 1;
			break;
		}
		if (a*a == b * b + c * c) printf("right\n");
		else if (b*b == a * a + c * c) printf("right\n");
		else if (c*c == a * a + b * b) printf("right\n");
		else printf("wrong\n");
	}

}