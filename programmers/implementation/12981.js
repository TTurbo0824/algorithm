// 프로그래머스 Summer/Winter Coding(~2018): 영어 끝말잇기
// https://programmers.co.kr/learn/courses/30/lessons/12981?language=javascript

function solution(n, words) {
  let answer = [0, 0];

  let start = words[0];
  const newArr = [start];

  for (let i = 1; i < words.length; i++) {
    if (words[i][0] !== start[start.length - 1]) {
      answer[0] = (i + 1) % n || n;
      if (answer[0] === n) answer[1] = parseInt((i + 1) / n);
      else answer[1] = parseInt((i + 1) / n) + 1;
      break;
    } else if (newArr.includes(words[i])) {
      answer[0] = (i + 1) % n || n;
      if (answer[0] === n) answer[1] = parseInt((i + 1) / n);
      else answer[1] = parseInt((i + 1) / n) + 1;
      break;
    }
    start = words[i];
    newArr.push(start);
  }

  return answer;
}
