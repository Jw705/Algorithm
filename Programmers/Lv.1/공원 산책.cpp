// 23.06.12

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer;
    for(int i=0;i<park.size();i++){
        for(int j=0;j<park[i].length();j++) {
            if(park[i][j]=='S'){
                answer.push_back(i);
                answer.push_back(j);                
            }
        }
    }
    
    for(string s:routes){
        string direction = s.substr(0,s.find(' '));
        int length = stoi(s.substr(s.find(' ')));
        
        int tmpy=answer[0];
        int tmpx=answer[1];
        
        int i=0;
        for(;i<length;i++){
            if(direction=="N"){
                tmpy-=1;
            } else if (direction=="S"){
                tmpy+=1;                
            } else if (direction=="W"){
                tmpx-=1;                
            } else if (direction=="E"){
                tmpx+=1;  
            }
            
            if(tmpx<0 || tmpy<0 || tmpx>=park[i].length() || tmpy>=park.size() || park[tmpy][tmpx]=='X'){
                break;              
            }
        }        
        if(i==length) {
            answer[0] = tmpy;
            answer[1] = tmpx;          
        }
    }
    
    return answer;
}