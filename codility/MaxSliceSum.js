function solution(A) {
  // maxNum에 초기값 0을 할당해준다
  let maxNum = 0;

  A.reduce((a, b) => {
    // 이전의 수를 합한 것(=누적된 값)과 현재 숫자를 더한 값을 temp라는 변수에 할당한다.
    let temp = a + b;

    // 만약 temp가 0보다 작다면 바로 0을 return한다

    // 0보다는 크지만 현재 maxNum보다 작다면 그 숫자를 시작으로
    // 계속 값을 누적시켜준다

    if (temp < 0) {
      return 0;
    } else if (temp < maxNum) {
      return temp;
    }

    // 그 이외의 경우(=maxNum보다 크다면) maxNum을 temp로 교체한다
    return (maxNum = temp);
  }, 0);

  // 만약 maxNum이 여전히 0이라면 이 경우는 A의 모든 요소가 음수라는 뜻이다
  // 그렇다면 A 중 가장 큰 숫자를 return하면 그 수가 자동적으로 가장 큰 누적값이 된다
  if (maxNum === 0) {
    return Math.max(...A);
  }
  // 그 외의 경우는 maxNum을 return 해준다.
  return maxNum;
}
