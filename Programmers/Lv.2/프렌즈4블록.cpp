#include <string>
#include <vector>
#include <iostream>

using namespace std;

int checkAndDel(int i, int j, int m, int n, vector<string> &board){
    
    if(board[i][j]!='-' &&
       board[i][j]==board[i][j+1] &&
       board[i][j]==board[i+1][j] &&
       board[i][j]==board[i+1][j+1]){
        
		if (j < n - 2)
			checkAndDel(i, j + 1, m, n, board);
		if (i < m - 2) {
			checkAndDel(i + 1, j, m, n, board);
		}
		if (i < m - 2 && j < n - 2)
			checkAndDel(i + 1, j + 1, m, n, board);
        
        board[i][j]='-';
        board[i][j+1]='-';
        board[i+1][j]='-';
        board[i+1][j+1]='-';
        
        for(string b : board){
            cout << b << endl;
        }
        cout << endl;
        return 1;
    }      
    else
        return 0;
}

void drop(int m, int n, vector<string> &board) {
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
	cout << "--------------" << endl;
	for (string b : board) {
		cout << b << endl;
	}
	cout <<"--------------"<< endl;
}

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    
    int a=0;
    int b=0; 
    while(a==0){
        b=0;
        
        for(int i=0;i<m-1;i++){
            for(int j=0;j<n-1;j++){
                int tmp = checkAndDel(i,j,m,n,board);
                b+=tmp;                 
            }
        }
        cout<<b<<endl;
        if(b!=a){
            drop(m,n,board);            
        }
        else{
            a=1;
        }
    }
    
    
    
    
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if (board[i][j] == '-')
                answer++;
        }
    }
    
    return answer;
}