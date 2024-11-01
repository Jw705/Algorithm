// 50m
class Queue {
  constructor() {
    this.inStack = [];
    this.outStack = [];
  }

  enqueue(item) {
    this.inStack.push(item);
  }

  dequeue() {
    if (this.outStack.length === 0) {
      while (this.inStack.length > 0) {
        this.outStack.push(this.inStack.pop());
      }
    }
    return this.outStack.pop();
  }

  size() {
    return this.inStack.length + this.outStack.length;
  }
}

const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");

// 입력값 처리
const [n, m] = input[0].split(" ").map(Number);
const graph = [];

const ghostList = [];
let [startX, startY] = [0, 0]; // 출발점의 좌표를 저장
let exit = [0, 0];

for (let i = 1; i < n + 1; i++) {
  graph.push(input[i]);
  for (let j = 0; j < m; j++) {
    if (input[i][j] === "G") {
      ghostList.push([i - 1, j]);
    } else if (input[i][j] === "N") {
      startX = i - 1;
      startY = j;
    } else if (input[i][j] === "D") {
      exit = [i - 1, j];
    }
  }
}

const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

const bfs = (startX, startY) => {
  const queue = new Queue();
  queue.enqueue([startX, startY, 0]);
  let length = 1000 * 1001;

  let visited = [];
  for (let i = 0; i < n; i++) {
    visited.push(Array(m).fill(false));
  }
  visited[startX][startX] = true;

  while (queue.size() > 0) {
    const [x, y, len] = queue.dequeue();

    // 도착점에 도착했으면, 정답에 1 추가
    if (graph[x][y] === "D") {
      length = len;
      break;
    }

    // 현재 위치에서 상하좌우로 이동
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
        continue;
      } else if (visited[nx][ny] === false && graph[nx][ny] !== "#") {
        visited[nx][ny] = true;
        queue.enqueue([nx, ny, len + 1]);
      }
    }
  }
  return length;
};

let min_namwoo_length = bfs(startX, startY);
let min_ghost_length = 1000 * 1001;

for (let i = 0; i < ghostList.length; i++) {
  const lenToExit =
    Math.abs(exit[0] - ghostList[i][0]) + Math.abs(exit[1] - ghostList[i][1]);
  min_ghost_length = Math.min(min_ghost_length, lenToExit);
}

if (min_namwoo_length < min_ghost_length) {
  console.log("Yes");
} else {
  console.log("No");
}

//console.log(min_namwoo_length, min_ghost_length)
