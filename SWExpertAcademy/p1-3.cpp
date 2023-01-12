#include <stdio.h>

typedef struct locate {
  int x;
  int y;
} loc;

int find_path(char map[][30], int visit[30], loc n, int cnt, int r, int c) {

  int max_rst = cnt;
  loc new_loc;
  int a[4] = {-1, 0, 1, 0};
  int b[4] = {0, 1, 0, -1};

  for (int i = 0; i < 4; i++) {

    new_loc.x = n.x + a[i];
    new_loc.y = n.y + b[i];
    if (new_loc.x >= r || new_loc.x < 0 || new_loc.y >= c || new_loc.y < 0)
      continue;

    int charr = map[new_loc.x][new_loc.y] - 'A';
    if (visit[charr] == 0) {

      visit[charr]++;
      int new_rst;
      new_rst = find_path(map, visit, new_loc, cnt + 1, r, c);
      if (new_rst == 26) {
        return 26;
      }
      max_rst = (max_rst < new_rst) ? new_rst : max_rst;

      visit[charr]--;
    }
  }
  return max_rst;
}

int main() {

  int T;
  scanf("%d", &T);
  for (int test_case = 0; test_case < T; test_case++) {
    int r, c;
    char map[30][30] = {
        0,
    };
    int visit[30] = {
        0,
    };
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        scanf(" %c", &map[i][j]);
      }
    }

    loc n;
    n.x = 0;
    n.y = 0;

    visit[map[0][0] - 'A']++;

    int rst;
    rst = find_path(map, visit, n, 1, r, c);
    printf("#%d %d\n", test_case + 1, rst);
  }
  return 0;
}