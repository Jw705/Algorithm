#include <string>
#include <vector>

using namespace std;

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    int todayInt 
        = stoi(today.substr(0,4))*28*12+(stoi(today.substr(5,7))-1)*28+stoi(today.substr(8,10));
    
    int i=1;
    for (string s : privacies){        
        int newDayInt = stoi(s.substr(0,4))*28*12
            +(stoi(s.substr(5,7))-1)*28+stoi(s.substr(8,10));
        
        for(string p : terms){
            if(s[11]==p[0]){
                newDayInt+=stoi(p.substr(2))*28;
                newDayInt-=1;
            }
        }
        
        if(newDayInt<todayInt){
            answer.push_back(i);
        }
        i++;        
    }
    
    return answer;
}