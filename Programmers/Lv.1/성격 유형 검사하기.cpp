#include <string>
#include <vector>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    char typeName[8]={'R','T','C','F','J','M','A','N'};
    int typeScore[8]={0};
    for(int i=0;i<survey.size();i++){
        if (choices[i]==1) {            
            for(int j=0;j<8;j++){
                if(typeName[j]==survey[i][0])
                    typeScore[j]+=3;
            }
        }
        else if (choices[i]==2) {            
            for(int j=0;j<8;j++){
                if(typeName[j]==survey[i][0])
                    typeScore[j]+=2;
            }
        }
        else if (choices[i]==3) {            
            for(int j=0;j<8;j++){
                if(typeName[j]==survey[i][0])
                    typeScore[j]+=1;
            }
        }

        else if (choices[i]==5) {            
            for(int j=0;j<8;j++){
                if(typeName[j]==survey[i][1])
                    typeScore[j]+=1;
            }
        }        
        else if (choices[i]==6) {            
            for(int j=0;j<8;j++){
                if(typeName[j]==survey[i][1])
                    typeScore[j]+=2;
            }
        }        
        else if (choices[i]==7) {            
            for(int j=0;j<8;j++){
                if(typeName[j]==survey[i][1])
                    typeScore[j]+=3;
            }
        }  
    }

    answer += typeScore[0] >= typeScore[1] ? 'R' : 'T';
    answer += typeScore[2] >= typeScore[3] ? 'C' : 'F';
    answer += typeScore[4] >= typeScore[5] ? 'J' : 'M';
    answer += typeScore[6] >= typeScore[7] ? 'A' : 'N';
    return answer;
}