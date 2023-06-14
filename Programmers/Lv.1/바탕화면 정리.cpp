#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    vector<int> answer;
    
    int lux = 100;
    int luy = 100;
    int rdx = 0;
    int rdy = 0;
    
    for(int i=0;i<wallpaper.size();i++){
        for(int j=0;j<wallpaper[i].length();j++){
            if(wallpaper[i][j]=='#'){
                if(i<lux)
                    lux=i;
                if(j<luy)
                    luy=j;
                if(i>rdx)
                    rdx=i;
                if(j>rdy)
                    rdy=j;
            }
        }  
    }
    
    answer.push_back(lux);
    answer.push_back(luy);
    answer.push_back(rdx+1);
    answer.push_back(rdy+1);
    return answer;
}