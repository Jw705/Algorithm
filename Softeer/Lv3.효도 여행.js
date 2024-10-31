const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const S = input[1];

const graph = Array.from({ length: n + 1 }, () => []);
for (let i = 2; i < n + 1; i++) {
  let [u, v, c] = input[i].split(" ");
  graph[Number(u)].push([Number(v), c]);
  graph[Number(v)].push([Number(u), c]);
}

let answer = 0;
const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
const visited = Array(n + 1).fill(false);

function findRoot(curNode, curRoute) {
  visited[curNode] = true;
  const curRouteLength = curRoute.length;

  if (curRoute.length > 0) {
    for (let i = 1; i <= m; i++) {
      if (S[i - 1] === curRoute[curRouteLength - 1]) {
        dp[i][curRouteLength] = dp[i - 1][curRouteLength - 1] + 1;
      } else {
        dp[i][curRouteLength] = Math.max(
          dp[i - 1][curRouteLength],
          dp[i][curRouteLength - 1]
        );
      }
    }
  }

  if (graph[curNode].length === 1 && curRoute.length > answer) {
    answer = Math.max(answer, dp[m][curRouteLength]);
  } else {
    for (let i = 0; i < graph[curNode].length; i++) {
      const [nextNode, nextC] = graph[curNode][i];
      if (visited[nextNode] === false) {
        findRoot(nextNode, curRoute + nextC);
      }
    }
  }
}

findRoot(1, "");
console.log(answer);
