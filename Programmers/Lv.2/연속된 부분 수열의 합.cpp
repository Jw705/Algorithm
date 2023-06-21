// 23.06.21

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    answer.push_back(1);
    answer.push_back(1000002);
    
    int i=0;
    int j=0;
    int sum=sequence[0];
    
    while (i <= j && j < sequence.size()){        
        if(sum >= k){ 
            if(sum == k){
                if(answer[1]-answer[0]>j-i){
                    answer[0]=i;
                    answer[1]=j;                
                }
                else if((answer[1]-answer[0])==(j-i) && i<answer[0]){
                    answer[0]=i;
                    answer[1]=j;                

                }
            }
            sum -= sequence[i];
            i++;
        }
        else{
            j++;
            sum += sequence[j];
        } 
    }
    
    return answer;
}