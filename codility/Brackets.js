// https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

function solution(S) {
  const temp = [];

  for (let i = 0; i < S.length; i++) {
    if (!temp && (S[i] === ']' || S[i] === '}' || S[i] === ')')) {
      return 0;
    } else if (S[i] === '(' || S[i] === '{' || S[i] === '[') {
      temp.push(S[i]);
    } else if (
      (temp[temp.length - 1] === '(' && S[i] === ')') ||
      (temp[temp.length - 1] === '{' && S[i] === '}') ||
      (temp[temp.length - 1] === '[' && S[i] === ']')
    ) {
      temp.pop();
    } else {
      return 0;
    }
  }
  if (temp.length !== 0) return 0;
  else return 1;
}
