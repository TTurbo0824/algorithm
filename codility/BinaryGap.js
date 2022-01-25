// https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

function solution(N) {
  // 최종적으로 출력해줄 answer 변수를 0으로 초기화
  let answer = 0;

  // 우선 정수 N을 2진수로 변환해 줌
  const bin = N.toString(2);

  // split 메서드를 사용하여 1을 기준으로 해당 수를 끊어 준다
  const splitBin = bin.split('1');

  // 만약 맨 앞 요소가 ''이 아니라면 해당 요소의 앞자리가 1이 아니었음을 의미함으로
  // 해당 요소는 binary gap의 조건을 충족하지 못함으로 제거해준다
  if (splitBin[0] !== '') {
    splitBin.shift();
  }

  // 마찬가지로 맨 뒤 요소가 ''이 아니라면 해당 요소의 뒷자리가 1이 아니었음을 의미함으로
  // 해당 요소는 binary gap의 조건을 충족하지 못함으로 제거해준다
  if (splitBin[splitBin.length - 1] !== '') {
    splitBin.pop();
  }

  // 만약 splitBin의 길이가 0이라면 binary gap의 조건을 충족시키는 요소가
  // 없었음을 의미, 0을 return 해준다
  if (splitBin.length === 0) return answer;
  // 그 외의 경우에는 forEach 메서드를 사용해서 splitBin을 순회하며
  // 최종적으로 가장 길이가 긴 요소의 길이를 return 해준다
  else {
    splitBin.forEach((el) => {
      if (answer < el.length) answer = el.length;
    });
  }

  return answer;
}
