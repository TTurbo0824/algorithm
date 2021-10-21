// 프로그래머스 완전탐색: 모의고사
// https://programmers.co.kr/learn/courses/30/lessons/42840

const answers = [1, 3, 2, 4, 2];

const solution = (answers) => {
  let answer = [];
  // 세 사람 모두 각각의 다른 패턴을 가지고 있음
  let first = [1, 2, 3, 4, 5];
  let second = [2, 1, 2, 3, 2, 4, 2, 5];
  let third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  // 이 패턴이 answers 배열을 담을 수 있도록 확장 시킴
  first = Array(Math.ceil(answers.length / first.length))
    .fill(first)
    .flat();
  second = Array(Math.ceil(answers.length / second.length))
    .fill(second)
    .flat();
  third = Array(Math.ceil(answers.length / third.length))
    .fill(third)
    .flat();

  let total = [0, 0, 0];

  // answer 배열을 순회하며 각각의 수포자들이 몇 문제나 맞추었는지 계산
  answers.map((el, idx) => {
    if (first[idx] === el) total[0] += 1;
    if (second[idx] === el) total[1] += 1;
    if (third[idx] === el) total[2] += 1;
  });

  // 최고점이 몇 점인지 도출 => Math.max(...total)
  // 이 최고점을 받은 사람이 몇 번 째 수포자인지 판별 후 answer 배열에 push 해줌
  total.map((el, idx) => {
    if (el === Math.max(...total)) answer.push(idx + 1);
  });

  return answer;
};
