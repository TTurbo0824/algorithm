// https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

function solution(A, B, K) {
  // 만약 A가 0이라면 B를 K로 나눈 값에 1을 더해준다.
  if (A === 0) return Math.floor(B / K) + 1;
  // 그렇지 않다면 1에서부터 B까지 K의 배수의 수에
  // A 이전에 나오는 K의 배수의 수를 빼주면 된다.
  else return Math.floor(B / K) - Math.floor((A - 1) / K);
}
