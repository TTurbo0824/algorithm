// https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/

function solution(N) {
  let answer = 0;

  for (let i = 1; i <= N ** 0.5; i++) {
    if (i * i === N) {
      answer++;
    } else if (N % i === 0) {
      answer += 2;
    }
  }
  return answer;
}
