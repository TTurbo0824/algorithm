// 프로그래머스 스택/큐: 기능개발
// https://programmers.co.kr/learn/courses/30/lessons/42586

function solution(progresses, speeds) {
  let answer = [];
  let day = new Array(progresses.length).fill();

  for (let i = 0; i < progresses.length; i++) {
    day[i] = Math.ceil((100 - progresses[i]) / speeds[i]);
  }

  // day 배열의 길이가 0보다 클 때까지 반복
  while (day.length > 0) {
    let finishIndex = day.findIndex((fn) => day[0] < fn);

    if (finishIndex === -1) {
      // 만약 찾지 못했다면 answer에 day 배열의 길이를 넣은 후, day 내부의 요소를 전부 삭제
      answer.push(day.length);
      day.splice(0, day.length);
    } else {
      // 만약 찾았다면, 해당 인덱스를 answer에 넣고, day에서 그만큼 제외
      answer.push(finishIndex);
      day.splice(0, finishIndex);
    }
  }

  return answer;
}
