// 프로그래머스 월간 코드 챌린지 시즌2: 음양 더하기
// https://programmers.co.kr/learn/courses/30/lessons/76501

const solution = (absolutes, signs) => {
  let answer = 0;

  absolutes.map((el, idx) => {
    signs[idx] === true ? (answer += el) : (answer -= el);
  });

  return answer;
};
