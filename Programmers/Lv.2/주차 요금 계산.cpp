#include <string>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    
    map<int,int> inputTime;
    map<int,int> totalTime;
    
    for(string s : records){
        int time = stoi(s.substr(0,2))*60 + stoi(s.substr(3,2));
        int carNum = stoi(s.substr(6,4));
        if(s.substr(11)=="IN"){
            if(totalTime.find(carNum)==totalTime.end()){
                inputTime.insert({carNum,time});
            }
            else {
                inputTime[carNum]=time;
            }
        }
        else if (s.substr(11)=="OUT"){
            if(totalTime.find(carNum)==totalTime.end()){
                totalTime.insert({carNum,time-inputTime[carNum]});
                inputTime[carNum]=0;
            }
            else {
                totalTime[carNum]+=time-inputTime[carNum];
                inputTime[carNum]=0;
            }
        }
    }
        
    for(pair<int,int> p : inputTime){
        if(0!=p.second){
            totalTime[p.first]+=60*24-1-p.second;            
        }
        if(totalTime.find(p.first)==totalTime.end()){
            totalTime.insert({p.first,60*24-1-p.second});
        }
    }
    
    
    for(pair<int,int> p : totalTime){        
        int cost = fees[1];
        if(fees[0]<p.second){
            cost+=ceil(double(p.second-fees[0])/fees[2])*fees[3];
        }
        answer.push_back(cost);
    }
    
    
    return answer;
}