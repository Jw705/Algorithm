const input = require("fs").readFileSync(0).toString().split("\n");

const [h, k, r] = input[0].split(" ").map(Number);

const graph = [];
for (let i = 0; i < Math.pow(2, h + 1); i++) {
  graph.push([]);
}
for (let i = 1; i <= Math.pow(2, h); i++) {
  graph[Math.pow(2, h) + i - 1] = input[i].split(" ").map(Number);
}

const updateWork = (node) => {
  if (node === 0) {
    if (graph[1].length > 0) {
      answer += graph[1].shift();
    }
    updateWork(1);
  } else {
    const lChild = node * 2;
    const rChild = node * 2 + 1;

    let target = -1;

    if (curDay % 2 === 0) {
      if (graph[rChild].length > 0) {
        target = rChild;
      }
    } else {
      if (graph[lChild].length > 0) {
        target = lChild;
      }
    }

    if (target !== -1) {
      graph[node].push(graph[target].shift());
    }

    if (node * 2 < Math.pow(2, h)) {
      updateWork(lChild);
      updateWork(rChild);
    }
  }
};

let answer = 0;
let day = 0;
for (; day < r; day++) {
  updateWork(0);
}

console.log(answer);

/*
2 5 1
1
2
3
4
5
6

3 5 1
1
2
3
4
5
6
7
8
*/
