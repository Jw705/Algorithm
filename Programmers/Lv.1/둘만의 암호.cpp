//23.06.22

#include <string>
#include <vector>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    for(int i=0;i<s.length();i++){
        for(int j=0;j<index;j++){
            
            if(s[i]=='z'){
                s[i]='a';                
            }
            else {
                s[i]++;                
            }
            
            while(skip.find(s[i]) != string::npos){
                if(s[i]=='z'){
                    s[i]='a';                
                }
                else {
                    s[i]++;                
                }               
            }
        }
    }
    answer = s;
    return answer;
}