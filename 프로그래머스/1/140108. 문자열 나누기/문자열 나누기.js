function solution(s) {
    var answer = 0; 
    let x = s[0]
    let cnt_same = 1
    let cnt_diff = 0
    let tmp=x
    
    for(let i=1;i<s.length;i++) {
        tmp=tmp+s[i]
        
        if (s[i]===tmp[0]) cnt_same++;
        else cnt_diff++;
        
        if (cnt_same===cnt_diff){
            tmp=''            
            cnt_same = 0
            cnt_diff = 0
            answer++
        }
    }    
    if (tmp.length>0) answer++
    return answer;
}