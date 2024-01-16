function solution(expression) {
  const plus = (arr) => arr.reduce((acc, cur) => acc + Number(cur), 0);
  const minus = (arr) => arr.reduce((acc, cur) => acc - Number(cur), 0) + Number(arr[0]) * 2;
  const multiply = (arr) => arr.reduce((acc, cur) => acc * cur, 1);
  const operators = ['+', '-', '*'];
  const operatorCalMap = {
    '+': plus,
    '-': minus,
    '*': multiply,
  };

  const allOperatorsOrders = [];

  const fillOperatorOrder = (curOperators, visited) => {
    if (curOperators.length === 3) {
      allOperatorsOrders.push([...curOperators]);
      return;
    }

    for (let i = 0; i < 3; i += 1) {
      if (!visited[i]) {
        visited[i] = 1;
        curOperators.push(operators[i]);
        fillOperatorOrder(curOperators, visited);
        curOperators.pop();
        visited[i] = 0;
      }
    }
  };

  fillOperatorOrder([], [0, 0, 0]);

  const processOperators = (string, remainOperators) => {
    if (!remainOperators.length) return string;

    const operator = remainOperators.pop();
    const splited = string.split(operator).map((el) => processOperators(el, remainOperators));
    const processed = operatorCalMap[operator](splited);
    remainOperators.push(operator);

    return processed;
  };

  const calculate = () => {
    let max = 0;

    for (const targetOperators of allOperatorsOrders) {
      max = Math.max(max, Math.abs(processOperators(expression, targetOperators)));
    }

    return max;
  };

  return calculate();
}