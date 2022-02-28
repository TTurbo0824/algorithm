// https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

function solution(X, A) {
  const s = new Set();

  for (let i = 0; i < A.length; i++) {
    const value = A[i];
    s.add(value);

    if (s.size === X) {
      return i;
    }
  }
  return -1;
}

// Wrong solution - performance tests failed.
/*
function solution(X, A) {
  let newArr = new Array(X).fill(0);

  for (let i = 0; i < A.length; i++) {
    newArr[A[i] - 1] = 1;

    if (!newArr.includes(0)) {
      return i;
    }
  }
  return -1;
}
*/