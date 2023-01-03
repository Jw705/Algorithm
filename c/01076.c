#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
// [baekjoon] 1076번 - 저항

int main() {

	char s[3][100];

	char c[10][20] = { "black","brown","red", "orange","yellow","green","blue","violet","grey","white" };
	scanf("%s", &s[0]);
	scanf("%s", &s[1]);
	scanf("%s", &s[2]);

	long long result = 0;
	
	if (strcmp(s[0], c[0]) == 0) result += 0;
	else if (strcmp(s[0], c[1]) == 0) result += 1;
	else if (strcmp(s[0], c[2]) == 0) result += 2;
	else if (strcmp(s[0], c[3]) == 0) result += 3;
	else if (strcmp(s[0], c[4]) == 0) result += 4;
	else if (strcmp(s[0], c[5]) == 0) result += 5;
	else if (strcmp(s[0], c[6]) == 0) result += 6;
	else if (strcmp(s[0], c[7]) == 0) result += 7;
	else if (strcmp(s[0], c[8]) == 0) result += 8;
	else if (strcmp(s[0], c[9]) == 0) result += 9;

	result *= 10;

	if (strcmp(s[1], c[0]) == 0) result += 0;
	else if (strcmp(s[1], c[1]) == 0) result += 1;
	else if (strcmp(s[1], c[2]) == 0) result += 2;
	else if (strcmp(s[1], c[3]) == 0) result += 3;
	else if (strcmp(s[1], c[4]) == 0) result += 4;
	else if (strcmp(s[1], c[5]) == 0) result += 5;
	else if (strcmp(s[1], c[6]) == 0) result += 6;
	else if (strcmp(s[1], c[7]) == 0) result += 7;
	else if (strcmp(s[1], c[8]) == 0) result += 8;
	else if (strcmp(s[1], c[9]) == 0) result += 9;
	
	if (strcmp(s[2], c[0]) == 0) result *= 1;
	else if (strcmp(s[2], c[1]) == 0) result *= 10;
	else if (strcmp(s[2], c[2]) == 0) result *= 100;
	else if (strcmp(s[2], c[3]) == 0) result *= 1000;
	else if (strcmp(s[2], c[4]) == 0) result *= 10000;
	else if (strcmp(s[2], c[5]) == 0) result *= 100000;
	else if (strcmp(s[2], c[6]) == 0) result *= 1000000;
	else if (strcmp(s[2], c[7]) == 0) result *= 10000000;
	else if (strcmp(s[2], c[8]) == 0) result *= 100000000;
	else if (strcmp(s[2], c[9]) == 0) result *= 1000000000;


	printf("%lld", result);

}