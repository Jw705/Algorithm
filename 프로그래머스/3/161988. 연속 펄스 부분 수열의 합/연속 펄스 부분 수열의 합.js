function solution(sequence) {
    let answer = 0;
    
    let prefix_sum1 = []
    let prefix_sum2 = []
    
    for(let i=0; i<sequence.length; i++) {
        if (i===0) {
            prefix_sum1.push(sequence[i])
            prefix_sum2.push(-sequence[i])
        } else if (i % 2 === 0){
            prefix_sum1.push(Math.max(prefix_sum1[i - 1] + sequence[i], sequence[i]))
            prefix_sum2.push(Math.max(prefix_sum2[i - 1] - sequence[i], -sequence[i]))
        } else {
            prefix_sum1.push(Math.max(prefix_sum1[i - 1] - sequence[i], -sequence[i]))
            prefix_sum2.push(Math.max(prefix_sum2[i - 1] + sequence[i], sequence[i]))
        }
        
        answer = Math.max(answer, prefix_sum1[i], prefix_sum2[i]);
    }
    
    return answer;
}