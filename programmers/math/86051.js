// 프로그래머스 월간 코드 챌린지 시즌3 없는 숫자 더하기
// https://programmers.co.kr/learn/courses/30/lessons/86051

const solution= (numbers) => {
  let answer = 0;
  const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  arr.map((el) => {
    if (!numbers.includes(el)) answer += el;
  });

  return answer;
}
