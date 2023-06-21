// 23.06.12

#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;
    
    for(int i=1;i<r2;i++){
        long long result=0;
        
        long long r1r1 = (long long)r1*r1;
        long long r2r2 = (long long)r2*r2;
        long long ii = (long long)i*i;
        
        long long a; // 안쪽 원 바깥 점 시작범위
        long long b; // 바깥 원 안쪽 점 마지막 범위
        
        b = floor(sqrt( abs((long long)r2r2-ii) ));  
        
        if(abs(i)<r1){
            a = ceil(sqrt( abs(((long long)r1r1-ii))));
            result = (b-a+1);
        }
        else{
            a = 1;
            result = (b-a+1);
        }
        
        answer+=result*4;
    }
    answer+=(r2-r1+1)*4;
    
    return answer;
}