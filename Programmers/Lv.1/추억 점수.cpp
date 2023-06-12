// 23.06.12
// https://sirius7.tistory.com/

#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    
    map<string, int> m1;
    for (int i=0;i<name.size(); i++){
        m1.insert(pair<string, int>(name[i], yearning[i]));
    }
    
    for (vector<string> v : photo) {
        int score = 0;
        for (string s : v) {
            score+=m1[s];
            /*
            map<string, int>::iterator it = m1.find(s);
            if(it != m1.end())
                score+=m1.find(s)->second;
            이렇게 복잡하게 풀지 않아도 된다.
            m1[s]에서 s가 key에 존재하지 않는 값이면 m1[s]=0 이다.
            */
        }
        answer.push_back(score);
    }
        
    return answer;
}