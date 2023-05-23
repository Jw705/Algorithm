#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    
    vector<string> answer(players);
    
    for(int i=0;i<callings.size();i++){
        int locate = find(answer.begin(), answer.end(), callings[i]) - answer.begin();
        string tmp = answer[locate];
        answer[locate] = answer[locate-1];
        answer[locate-1] = tmp;
    }
    
    return answer;
}