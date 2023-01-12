#include <stdio.h>
#include <string.h>

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    char N[100005];
    int map[100005];
    int x, y;
    int N_len;
    scanf("%s", N);
    N_len = (int)strlen(N);
    scanf("%d %d", &x, &y);

    int a, b;
    a = (x > y) ? y : x;
    b = (x > y) ? x : y;

    int flag2 = 0;
    for (int j = 0; j < N_len; j++) {

      if (flag2 == 1) {
        map[j] = 2;
        continue;
      }

      if (N[j] - '0' > b) {
        map[j] = 2;
        flag2 = 1;
      }
      if (N[j] - '0' == b) {
        map[j] = 2;
      }
      if (N[j] - '0' > a && N[j] - '0' < b) {
        map[j] = 1;
        flag2 = 1;
      }
      if (N[j] - '0' == a) {
        map[j] = 1;
      }
      if (N[0] - '0' < a) {
        if (N_len == 1) {
          map[0] = -1;
        } else {
          map[0] = 0;
          flag2 = 1;
        }
        continue;
      }

      if (N[j] - '0' < a && j != 0) {
        map[j] = 2;
        flag2 = 1;
        int flag1 = 0;
        for (int k = j - 1; k >= 0; k--) {

          if (map[k] == 1 && k == 0) {
            map[k] = 0;
            break;
          }
          if (map[k] == 1) {
            map[k] = 2;

            continue;
          }
          if (map[k] == 2) {
            map[k] = 1;

            break;
          }
        }
      }
    }

    int flag3 = 0;
    printf("#%d ", i + 1);
    for (int j = 0; j < N_len; j++) {
      if (map[0] == 1 && N_len == 1 && a == 0) {
        printf("-1");
        break;
      }
      if (map[j] == 1 && a == 0 && flag3 == 0) {
        continue;
      }
      if (map[j] == 0 && flag3 == 0) {

        continue;
      } else {
        flag3 = 1;
        if (map[j] == 2)
          printf("%d", b);
        if (map[j] == 1)
          printf("%d", a);
        if (map[j] == -1)
          printf("-1");
      }
    }
    printf("\n");
  }

  return 0;
}