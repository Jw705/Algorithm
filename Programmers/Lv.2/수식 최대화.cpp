// 23.06.22

#include <string>
#include <vector>

using namespace std;

long long calc(long long a, long long b, char op) {
    if (op == '+')
        return a + b;
    else if (op == '-')
        return a - b;
    else if (op == '*')
        return a * b;
}

long long solution(string expression) {
    long long answer = 0;
    
    int priority[6][3]={
        {0,1,2},{0,2,1},
        {1,0,2},{1,2,0},
        {2,0,1},{2,1,0}            
    };
       
    vector<long long> num;
    vector<char> oper;
    
    string n ="";
    for(int i=0;i<expression.length();i++){
        if (expression[i]=='+'||expression[i]=='-'||expression[i]=='*'){
            num.push_back(stoi(n));
            n = "";
            oper.push_back(expression[i]);
        }
        else{
            n+=expression[i];
        }
    }    
    num.push_back(stoi(n));
    
    string op = "+-*";
    for (int i=0; i<6; i++){    
        vector<long long> tmp_num = num;
        vector<char> tmp_oper = oper;
        
        for (int j=0; j<3; j++){
            for (int k=0; k<tmp_oper.size();){
                if(tmp_oper[k]==op[priority[i][j]]){
                    long long result = calc(tmp_num[k],tmp_num[k+1],tmp_oper[k]);
                    tmp_num.erase(tmp_num.begin() + k);
                    tmp_num.erase(tmp_num.begin() + k);
                    tmp_num.insert(tmp_num.begin() + k, result);    
                    tmp_oper.erase(tmp_oper.begin() + k);                    
                }
                else {
                    k++;
                }
            }
        }
        
        if(tmp_num[0]<0)
            tmp_num[0]*=-1;
        if(tmp_num[0]>answer)
            answer = tmp_num[0];
    }
    
    return answer;
}