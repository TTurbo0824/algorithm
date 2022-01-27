// https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

function solution(A) {
  let answer = 1;
  A = new Set([...A]);
  let newArr = [...A];
  newArr = newArr.sort((a, b) => a - b);
  newArr = newArr.filter((el) => el > 0);
  const arrLength = newArr.length;

  if (arrLength === 0) {
    return answer;
  } else if (arrLength === 1) {
    if (newArr[0] === 1) return 2;
    else return answer;
  }
  if (newArr[0] !== 1) return answer;
  else if (arrLength === newArr[arrLength - 1] - newArr[0] + 1) {
    if (newArr[arrLength - 1] !== arrLength + 1) return arrLength + 1;
    else {
      newArr = newArr.sort((a, b) => a - b);
      let totalSum = newArr.reduce((a, b) => a + b);
      let expectedSum = (newArr[0] + newArr[arrLength - 1]) * 0.5 * (arrLength + 1);
      return expectedSum - totalSum;
    }
  } else {
    for (let i = 0; i < arrLength; i++) {
      if (newArr[i] !== i + 1) {
        answer = newArr[i - 1] + 1;
        break;
      }
    }
    return answer;
  }
}
