#include < iostream >
#include < vector >
using namespace std;
int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, -1, 1};
int R, C, answer = 0;
bool inside(int r, int c) {
	return r >= 0 && r < R && c >= 0 && c < C;
}

void dfs(int r, int c, int cnt, int visited, vector< vector< char >> &cities) {
	answer = max(answer, cnt);

	for(int d = 0;d < 4;d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		if(!inside(nr, nc)) continue;
		if(visited & (1 << (cities[nr][nc] - 'A'))) continue;
		dfs(nr, nc, cnt + 1, visited | (1 << (cities[nr][nc] - 'A')), cities); 
	}
}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	// freopen("sample_input.txt", "r", stdin);
	cin >>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
		cin >> R >> C;
		answer = 0;
		vector< vector< char >> cities(R, vector< char >(C));
		for(int i = 0;i < R;i++) {
			for(int j = 0;j < C;j++) {
				cin >> cities[i][j];
			}
		}
		dfs(0, 0, 1, 1 << (cities[0][0] - 'A'), cities);

		cout << "#" << test_case << " " << answer << '\n';

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
