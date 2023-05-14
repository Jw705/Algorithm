#include <string>
#include <vector>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    char list[8]={'R','T','C','F','J','M','A','N'};
    int RTCFJMAN[8]={0};
    for(int i=0;i<survey.size();i++){
        if (choices[i]==1) {            
            for(int j=0;j<8;j++){
                if(list[j]==survey[i][0])
                    RTCFJMAN[j]+=3;
            }
        }
        else if (choices[i]==2) {            
            for(int j=0;j<8;j++){
                if(list[j]==survey[i][0])
                    RTCFJMAN[j]+=2;
            }
        }
        else if (choices[i]==3) {            
            for(int j=0;j<8;j++){
                if(list[j]==survey[i][0])
                    RTCFJMAN[j]+=1;
            }
        }

        else if (choices[i]==5) {            
            for(int j=0;j<8;j++){
                if(list[j]==survey[i][1])
                    RTCFJMAN[j]+=1;
            }
        }        
        else if (choices[i]==6) {            
            for(int j=0;j<8;j++){
                if(list[j]==survey[i][1])
                    RTCFJMAN[j]+=2;
            }
        }        
        else if (choices[i]==7) {            
            for(int j=0;j<8;j++){
                if(list[j]==survey[i][1])
                    RTCFJMAN[j]+=3;
            }
        }  
    }

    answer += RTCFJMAN[0] >= RTCFJMAN[1] ? 'R' : 'T';
    answer += RTCFJMAN[2] >= RTCFJMAN[3] ? 'C' : 'F';
    answer += RTCFJMAN[4] >= RTCFJMAN[5] ? 'J' : 'M';
    answer += RTCFJMAN[6] >= RTCFJMAN[7] ? 'A' : 'N';
    return answer;
}