// 프로그래머스 Summer/Winter Coding(~2018): 숫자 게임
// https://programmers.co.kr/learn/courses/30/lessons/12987

function solution(A, B) {
  var answer = 0;
  A.sort((a, b) => a - b);
  B.sort((a, b) => a - b);

  var temp = 0;
  for (var i = 0; i < A.length; i++) {
    for (var j = temp; j < B.length; j++) {
      if (A[i] < B[j]) {
        answer++;
        temp = j + 1;
        break;
      }
    }
  }

  return answer;
}
