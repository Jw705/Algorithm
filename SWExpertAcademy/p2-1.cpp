#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

const vector<vector<int>> drc = {
    // wasd
    {-1, 0}, {0, -1}, {1, 0}, {0, 1}
};

void Init();
int Dfs(const int r, const int c, const int visited);

int R, C;
vector<vector<int>> board;
vector<vector<unordered_map<int, int>>> dp;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; t++) {
        Init();
        cout << '#' << t << ' ' << Dfs(0, 0, 0) << ' ' << '\n';
    }
    return 0;
}

void Init() {
    cin >> R >> C;
    
    board.resize(R);
    for (int r = 0; r < R; r++) {
        board[r].resize(C);
        for (int c = 0; c < C; c++) {
            char ch;
            cin >> ws >> ch;
            board[r][c] = ch - 'A';
        }
    }
    
    dp.resize(R);
    for (int r = 0; r < R; r++) {
        dp[r].resize(C);
        for (int c = 0; c < C; c++) {
            dp[r][c] = {};
        }
    }
}

int Dfs(const int r, const int c, const int visited) {
    const int bit = 1 << board[r][c];
    if (visited & bit) {
        return 0;
    }
    if (dp[r][c].find(visited) != dp[r][c].end()) {
        return dp[r][c][visited];
    }
    int max_answer = 0;
    for (int d = 0; d < 4; d++) {
        const int nr = r + drc[d][0],
                nc = c + drc[d][1];
        if (nr >= 0 && nr < R
                && nc >= 0 && nc < C) {
            max_answer = max(max_answer, Dfs(nr, nc, visited | bit));
        }
    }
    dp[r][c][visited] = ++max_answer;
    return max_answer;
}