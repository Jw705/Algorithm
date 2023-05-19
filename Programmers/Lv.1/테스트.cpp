#include<iostream>
#include<string>
#include<map>
using namespace std;
 
int main(void){
    
    // 선언
    map<int, string> m1;
    
    // 삽입
    m1.insert(pair<int, string>(1, "samsung"));
    m1.insert(pair<int, string>(54, "apple"));
    // 이렇게도 삽입 가능
    m1[12] = "lg";
    m1[23] = "sony";
    
    // 탐색(접근)
    cout << m1[1].first << " , " << m1[1].second << "\n"    
    cout << m1[12].first << " , " << m1[12].second << "\n"
    
    map<int, string>::iterator iter;
    
    //접근방법 1 
    for(iter = m.begin(); iter != m.end(); iter++){
        cout << "[" << iter->first << ", " << iter->second << "]" << " " ;
    }
    cout << endl;
    
    //접근방법 2 
    for(iter = m.begin(); iter != m.end(); iter++){
        cout << "[" << (*iter).first << ", " << (*iter).second << "]" << " " ;
    }
    
    
    return 0;    
}
