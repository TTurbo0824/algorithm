// https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

function solution(A) {
  // 현재 A의 길이를 변수 arrLength를 생성해 할당해준다
  const arrLength = A.length;

  // Edge case handling
  // 만약 A가 빈배열이라면 자동적으로 빠진 숫자는 1이 된다
  // 만약 A의 길이가 1이라면 두 가지 경우에 수가 나오는데,
  // 1이 빠진 경우와 2가 빠진 경우로 나뉜다.
  // 맨 앞자리 요소가 1이라면 2, 2라면 1을 return 해준다.
  if (arrLength <= 0) {
    return 1;
  } else if (arrLength === 1) {
    return A[0] === 1 ? 2 : 1;
  }

  // 시간 효율성을 위해 가우스 공식을 응용해 풀이했다.

  // A를 sort() 메서드를 사용해 정렬해준다.
  A.sort((a, b) => a - b);

  // 현재 A의 모든 요소의 합을 reduce() 메서드를 사용해 구한 후 totalSum 변수에 할당한다.
  let totalSum = A.reduce((a, b) => a + b);

  // 만약 첫번째 요소가 1이 아니라면 자동적으로 1을 return 한다.

  // 만약 마지막 요소가 A 길이에 1을 더한 것이 아니라면
  // 마지막 숫자가 빠진 것임으로
  // A 길이에 1을 더한 값을 return 한다.

  // 두 가지 경우에 해당하지 않는다면 가우스 공식을 사용해
  // 숫자가 빠지기 전 모든 수의 합을 구한다
  // expectedSum에 totalSum을 빼면 그 수가 missing number가 된다.
  if (A[0] !== 1) {
    return 1;
  } else if (A[arrLength - 1] !== arrLength + 1) {
    return arrLength + 1;
  } else {
    let expectedSum = (A[0] + A[arrLength - 1]) * 0.5 * (arrLength + 1);

    return expectedSum - totalSum;
  }
}
