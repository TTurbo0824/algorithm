// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

function solution(A) {
  let obj = {};

  for (let i = 0; i < A.length; i++) {
    obj[A[i]] = !obj[A[i]];
  }

  for (let i = 0; i < A.length; i++) {
    if (obj[A[i]]) {
      return A[i];
    }
  }
  return null;
}
