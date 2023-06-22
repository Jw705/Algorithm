// 23.06.22

#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    
    int left=10;
    int right=11;
    
    int length[9][12] = 
    {
        {0,4,3,4,3,2,3,2,1,2,1,1},
        {},
        {3,1,0,1,2,1,2,3,2,3,4,4},
        {},
        {},
        {2,2,1,2,1,0,1,2,1,2,3,3},
        {},
        {},
        {1,3,2,3,2,1,2,1,0,1,2,2}
    };
    
    for (int n : numbers){
        if(n==1||n==4||n==7){
            answer += "L";
            left = n;
        }
        else if(n==3||n==6||n==9){
            answer += "R";
            right = n;
        }
        else{
            int left_length=length[n][left];
            int right_length=length[n][right];
            if(left_length<right_length){
                answer += "L";             
                left = n;   
            }
            else if(left_length>right_length){
                answer += "R";
                right = n;
            }
            else {
                if(hand=="left"){
                    answer += "L";
                    left = n;                
                }
                else{
                    answer += "R";
                    right = n;
                }
            }
            
        }
    }
    return answer;
}