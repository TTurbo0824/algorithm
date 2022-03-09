// 프로그래머스 완전탐색: 카펫
// https://programmers.co.kr/learn/courses/30/lessons/42842

function solution(brown, yellow) {
  const total = brown + yellow;

  const allCases = [];

  for (let i = 3; i < total; i++) {
    const divideNum = total / i;
    if (Math.floor(divideNum) === divideNum && i >= divideNum) {
      allCases.push([i, divideNum]);
    }
  }
  for (const carpetCase of allCases) {
    const [width, height] = carpetCase;
    const yellowNum = (width - 2) * (height - 2);

    if (yellowNum === yellow) {
      return carpetCase;
    }
  }
}

function solution(brown, yellow) {
  for (let i = 3; i <= (brown + yellow) / i; i++) {
    let x = Math.floor((brown + yellow) / i);
    if ((x - 2) * (i - 2) === yellow) {
      break;
    }
  }

  return [x, i];
}
