#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1924¹ø - 2007³â

int main() {

	int a, b;
	scanf("%d %d", &a, &b);

	int d = 0;

	switch (a) {
	case 12:
		d += 30;
	case 11:
		d += 31;
	case 10:
		d += 30;
	case 9:
		d += 31;
	case 8:
		d += 31;
	case 7:
		d += 30;
	case 6:
		d += 31;
	case 5:
		d += 30;
	case 4:
		d += 31;
	case 3:
		d += 28;
	case 2:
		d += 31;
	case 1:
		break;
	}

	d += b;
	d %= 7;

	switch (d) {
	case 0:
		printf("SUN");
		break;
	case 1:
		printf("MON");
		break;
	case 2:
		printf("TUE");
		break;
	case 3:
		printf("WED");
		break;
	case 4:
		printf("THU");
		break;
	case 5:
		printf("FRI");
		break;
	case 6:
		printf("SAT");
		break;
	}

}