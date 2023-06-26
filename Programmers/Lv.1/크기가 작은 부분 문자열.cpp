// 23.06.23

#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    for(int i=0;i<t.length()-(p.length()-1);i++){
        long long t_int=stoll(t.substr(i,p.length()));
        long long p_int=stoll(p);
        if(t_int<=p_int){
            answer++;
        }
    }
    
    return answer;
}