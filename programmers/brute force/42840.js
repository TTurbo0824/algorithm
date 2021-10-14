// 프로그래머스 완전탐색: 모의고사
// https://programmers.co.kr/learn/courses/30/lessons/42840

const answers = [1, 3, 2, 4, 2];

const solution = (answers) => {
  let answer = [];
  // 세 사람 모두 각각의 다른 패턴을 가지고 있음
  // 1번 다섯 숫자가 반복
  // 2번 여덟 숫자가 반복
  // 3번 열 개의 숫자가 반복
  // 주어진 answers라는 배열의 길이를 포함 수 있는 새로운 배열을 생성해서 진행
  // 패턴의 길이가 제각각이기 때문에 통일할 수 있는 방법이 없어 보임

  let first = [1, 2, 3, 4, 5];
  let second = [2, 1, 2, 3, 2, 4, 2, 5];
  let third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

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

  answers.map((el, idx) => {
    if (first[idx] === el) total[0] += 1;
    if (second[idx] === el) total[1] += 1;
    if (third[idx] === el) total[2] += 1;
  });

  // 최대값을 구해야함 => Math.max(...total)

  total.map((el, idx) => {
    if (el === Math.max(...total)) answer.push(idx + 1);
  });

  return answer;
};

console.log(solution(answers));

// let first = [1, 2, 3, 4, 5];

let first = [1, 2, 3, 4, 5];
let second = [2, 1, 2, 3, 2, 4, 2, 5];
let third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

// console.log(Array(Math.ceil(answers.length/first.length)).fill(first).flat() )
