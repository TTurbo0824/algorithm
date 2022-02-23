// https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

function solution(A) {
  const newArr = [...A];
  const set = new Set([...newArr]);
  const checkIndex = [];

  if (A.length !== [...set].length) {
    return 0;
  }

  for (let i = 0; i < A.length; i++) {
    if (A[i] > A.length || checkIndex.includes[A[i]]) {
      return 0;
    }
    checkIndex.push(A[i]);
  }
  return 1;
}
