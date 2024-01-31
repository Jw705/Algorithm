#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1259번 - 팰린드롬수

int main() {
	
	int n = 1;
	scanf("%d", &n);
	while (n != 0) {
		int s[5] = { 0 };
		int n2 = n;
		for (int i = 0; i < 5; i++) {
			s[i] = n2 % 10;
			n2 /= 10;
		}		
		if (n < 10) printf("yes\n");
		else if (n < 100) {
			if (s[0] == s[1])printf("yes\n");
			else printf("no\n");
		}
		else if (n < 1000) {
			if (s[0] == s[2])printf("yes\n");
			else printf("no\n");
		}
		else if (n < 10000) {
			if (s[0] == s[3] && s[1] == s[2])printf("yes\n");
			else printf("no\n");
		}
		else if (n < 100000) {
			if (s[0] == s[4] && s[1] == s[3])printf("yes\n");
			else printf("no\n");
		}
			   
		scanf("%d", &n);
	}


}