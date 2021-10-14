// 프로그래머스 연습문제: 콜라츠 추측
// https://programmers.co.kr/learn/courses/30/lessons/12943

const solution = (num) => {
  var answer = 0;

  while (true) {
    if (num === 1) break;

    // num의 특성 (짝수 or 홀수)에 따라 다른 연산이 필요
    if (num % 2 === 0) num /= 2;
    else num = num * 3 + 1;

    answer += 1;

    // answer가 500이 될 경우에 answer는 -1이 되고 반복문을 종료
    if (answer === 500) {
      answer = -1;
      break;
    }
  }

  return answer;
};
