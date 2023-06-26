// 23.06.24

#include <string>
#include <vector>

using namespace std;

int checkAndDel(int i, int j, int m, int n, vector<string> &board, int (&delBlock)[31][31]){
    
    if(board[i][j]!='-' &&
       board[i][j]==board[i][j+1] &&
       board[i][j]==board[i+1][j] &&
       board[i][j]==board[i+1][j+1]){
        
        delBlock[i][j]=1;
        delBlock[i][j+1]=1;
        delBlock[i+1][j]=1;
        delBlock[i+1][j+1]=1;
        
        return 1;
    }      
    else
        return 0;
}

void drop(int m, int n, vector<string> &board, int(&delBlock)[31][31]) {
	for (int i = 1; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j] == '-') {   
				for (int k = i; k > 0; k--) {
					char tmp = board[k][j];
					board[k][j] = board[k - 1][j];
					board[k - 1][j] = tmp;
				}
			}
		}
	}
}

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    
    int a=0;
    int b=0; 
    while(a==0){
        b=0;
        int delBlock[31][31]={0,};
        for(int i=0;i<m-1;i++){
            for(int j=0;j<n-1;j++){
                int tmp = checkAndDel(i,j,m,n,board,delBlock);
                b+=tmp;                 
            }
        }
        if(b!=a){
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (delBlock[i][j] == 1)
                        board[i][j] = '-';
                }
            }
            drop(m,n,board,delBlock);            
        }
        else
            a=1;
    }
    
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if (board[i][j] == '-')
                answer++;
        }
    }
    
    return answer;
}