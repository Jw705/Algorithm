const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;

rl.on("line", function (line) {
  input = line;
  rl.close();
}).on("close", function () {
  solution(input);
  process.exit();
});

function solution(input) {
  const [n, m] = input.split(" ").map((v) => parseInt(v));
  const max = Math.max(n, m);
  const min = Math.min(n, m);
  let cnt = 0;
  cnt += min - 1;
  cnt += (max - 1) * min;
  console.log(cnt);
}

let test = "2 2";
solution(test);
