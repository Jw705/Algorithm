const fs = require("fs");
const [k, p, n] = fs.readFileSync(0).toString().split(" ").map(BigInt);

let answer = k;
for (let i = 0; i < n; i++) {
  answer = (answer * p) % BigInt(1000000007);
}

console.log(Number(answer));
