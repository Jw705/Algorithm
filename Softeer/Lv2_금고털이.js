const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");

let [w, n] = input[0].split(" ").map(Number);
const price_info = [];

for (let i = 1; i < 1 + n; i++) {
  price_info.push(input[i].split(" ").map(Number));
}
price_info.sort((a, b) => b[1] - a[1]);

let answer = 0;
let idx = 0;
while (w > 0) {
  if (price_info[idx][0] <= w) {
    w -= price_info[idx][0];
    answer += price_info[idx][0] * price_info[idx][1];
  } else {
    answer += w * price_info[idx][1];
    w = 0;
  }
  idx++;
}
console.log(answer);
