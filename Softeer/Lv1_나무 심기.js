const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");

const n = Number(input[0]);
const F = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const answer = Math.max(F[0] * F[1], F[F.length - 1] * F[F.length - 2]);
console.log(answer);
