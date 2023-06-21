#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    for(string s : targets) {
        int total_Count = 0;
        for(char c : s){
            
            int type_count = 101;
            for(string k : keymap) {
                if(k.find(c)!=string::npos && k.find(c)<type_count){
                    type_count = k.find(c);
                }
            }
            
            if(type_count==101) {
                total_Count = -1;
                break;
            }
            else{
                total_Count += (type_count+1); 
            }            
            
        }        
        
        answer.push_back(total_Count);
        
    }
    return answer;
}