// 55m 시작

const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");

const [n, q] = input[0].split(" ").map(Number);
const yeonbi = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const dict = {};
for (let i = 0; i < n; i++) {
  dict[yeonbi[i]] = i * (n - i - 1);
}

for (let i = 2; i < 2 + q; i++) {
  carNum = Number(input[i]);
  if (carNum in dict) {
    console.log(dict[carNum]);
  } else {
    console.log(0);
  }
}
