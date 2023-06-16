// 23.06.16

#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    
    int paintEnd=0;
    for(int i : section){
        if(i>paintEnd){
            paintEnd = i+m-1;  
            answer++;
        }        
    }
    return answer;
}