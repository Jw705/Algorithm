#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    map<int,string> m_name; // 순위가 key, 이름이 value
    map<string,int> m_rank; // 이름이 key, 순위가 value
    for(int i=0;i<players.size();i++)
    {
        m_name[i] = players[i];
        m_rank[players[i]] = i;
    }
    
    for(int i=0;i<callings.size();i++){
        int locate = m_rank[callings[i]];           // 현재 해설이 부른 선수의 순위
        string prevPlayerName = m_name[locate-1];   // 그 선수 앞에 있는 선수의 이름
            
        m_name[locate-1] = callings[i];
        m_name[locate] = prevPlayerName;
        m_rank[callings[i]] = locate-1;
        m_rank[prevPlayerName] = locate;
    }
    
    // m_name의 모든 value를 answer에 넣어준다.
    for(auto c : m_name) 
        answer.push_back(c.second);
    
    return answer;
}