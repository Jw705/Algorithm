const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const graph = [];
for (let i = 1; i < 1 + n; i++) {
  const sum = input[i]
    .split(" ")
    .map(Number)
    .reduce((acc, num) => acc + num, 0);
  graph.push(sum);
}
const [L1, R1] = input[n + 1].split(" ").map(Number);
const [L2, R2] = input[n + 2].split(" ").map(Number);

for (let i = L1 - 1; i < L1 + 4; i++) {
  if (graph[i] > 0) graph[i] -= 1;
}
for (let i = L2 - 1; i < L2 + 4; i++) {
  if (graph[i] > 0) graph[i] -= 1;
}

console.log(graph.reduce((acc, num) => (acc += num), 0));
