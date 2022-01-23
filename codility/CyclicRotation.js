// https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

function solution(A, K) {
  const LEN = A.length;

  const N = K > LEN ? K % LEN : K;

  if (N === 0 || LEN <= 1) return A;
  else if (LEN === 2) {
    return N === 1 ? A.reverse() : A;
  } else {
    return [...A.slice(LEN - N, LEN), ...A.slice(0, LEN - N)];
  }
}
