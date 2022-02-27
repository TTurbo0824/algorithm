// 프로그래머스 완전탐색: 소수 찾기
// https://programmers.co.kr/learn/courses/30/lessons/42839

function solution(numbers) {
  const arr = numbers.split('');
  const answer = new Set();

  getNumber(arr, '');

  function getNumber(numberArr, currentNumber) {
    if (numberArr.length) {
      for (let i = 0; i < numberArr.length; i++) {
        const temp = [...numberArr];
        temp.splice(i, 1);

        if (isPrime(parseInt(currentNumber + numberArr[i]))) {
          answer.add(parseInt(currentNumber + numberArr[i]));
        }
        getNumber(temp, currentNumber + numberArr[i]);
      }
    }
  }

  return answer.size;
}

function isPrime(num) {
  if (num < 2) return false;
  if (num === 2) return true;
  for (let i = 2; i <= num ** 0.5; i++) {
    if (num % i === 0) return false;
  }
  return true;
}
