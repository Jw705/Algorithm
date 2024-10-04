function solution(X, A) {
  let left_leaf = X;
  let leafList = [];
  for (let i = 0; i <= X; i++) {
    leafList.push(false);
  }
  for (let i = 0; i < A.length; i++) {
    if (leafList[A[i]] == false) {
      leafList[A[i]] = true;
      left_leaf -= 1;
    }
    if (left_leaf == 0) {
      return i;
    }
  }
  return -1;
}
