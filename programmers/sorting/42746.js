// https://programmers.co.kr/learn/courses/30/lessons/42746

// Solution 1
/*
function solution(numbers) {
  var answer = numbers
    .map((c) => c + '')
    .sort((a, b) => b + a - (a + b))
    .join('');

  return answer[0] === '0' ? '0' : answer;
}
*/

// Solution 2
function solution(numbers) {
  const answer = numbers
    .sort((a, b) => {
      a = a.toString();
      b = b.toString();
      return b + a - (a + b);
    })
    .join('');

  return answer[0] === '0' ? '0' : answer;
}
