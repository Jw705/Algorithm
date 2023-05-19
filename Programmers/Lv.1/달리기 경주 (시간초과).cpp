#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    
    for(int i=0;i<callings.size();i++){
        int locate = find(players.begin(), players.end(), callings[i]) - players.begin();
        string tmp = players[locate];
        players[locate] = players[locate-1];
        players[locate-1] = tmp;
    }
    
    vector<string> answer(players);
    return answer;
}

// 시간복잡도 줄이기