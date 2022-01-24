// https://app.codility.com/programmers/lessons/6-sorting/distinct/

// Solution 1

function solution(A) {
  let arr = [];
  for (let i = 0; i < A.length; i++) {
    if (!arr.includes(A[i])) {
      arr.push(A[i]);
    }
  }
  return arr.length;
}

// Solution 2

```
function solution(A) {
  const newSet = new Set(A);
  return [...newSet].length;
}
```;
