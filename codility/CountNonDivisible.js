// https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/

function solution(A) {
  const arrLength = A.length;
  let numCnt = [...new Array(arrLength * 2 + 1)].map((_) => 0);

  for (let i in A) {
    numCnt[A[i]]++;
  }

  console.log(numCnt);
  let answer = [];
  for (let i = 0; i < arrLength; i++) {
    let divisors = 0;
    for (let j = 1; j <= A[i] ** 0.5; j++) {
      if (A[i] % j === 0) {
        divisors += numCnt[j];

        if (A[i] / j !== j) {
          divisors += numCnt[A[i] / j];
        }
      }
    }
    answer[i] = arrLength - divisors;
  }
  return answer;
}
