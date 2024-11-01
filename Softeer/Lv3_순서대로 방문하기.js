// 50m
const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");

// 입력값 처리
const [n, m] = input[0].split(" ").map(Number);
const graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i].split(" ").map(Number));
}
let [startX, startY] = [0, 0]; // 출발점의 좌표를 저장
for (let i = n + 1, j = 2; i < n + 1 + m; i++, j++) {
  const [x, y] = input[i].split(" ").map(Number);
  graph[x - 1][y - 1] = j;
  if (j === 2) {
    startX = x - 1;
    startY = y - 1;
  }
}

let result = 0;

const visited = [];
for (let i = 0; i < n; i++) {
  visited.push(Array(n).fill(false));
}
visited[startX][startY] = true;

const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

const dfs = (x, y, target) => {
  // 도착점에 도착했으면, 정답에 1 추가
  if (target === 2 + m) {
    result = result + 1;
    return;
  }

  // 현재 위치에서 상하좌우로 이동
  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
      continue;
    } else if (visited[nx][ny] === false) {
      if (graph[nx][ny] === 0) {
        visited[nx][ny] = true;
        dfs(nx, ny, target);
        visited[nx][ny] = false;
      } else if (graph[nx][ny] === target) {
        visited[nx][ny] = true;
        dfs(nx, ny, target + 1);
        visited[nx][ny] = false;
      }
    }
  }
};
dfs(startX, startY, 3);
console.log(result);
