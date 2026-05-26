# Chapter 4: Trees, Graphs, BFS & DFS

Traversing hierarchical (trees) and networked (graphs) structures is a major component of backend engineering interviews. This chapter covers **Breadth-First Search (BFS)** for level-by-level traversal, **Depth-First Search (DFS)** for deep path analysis, and **Topological Sort** for resolving dependency schedules.

---

##  Queue-based Level Traversal (BFS)

### Concept:
BFS explores nodes layer-by-layer. We utilize a **Queue** (First-In, First-Out) data structure to keep track of child nodes. It is the optimal strategy for finding the shortest path in unweighted graphs or level-order summaries in trees.

### 📐 ASCII Visualization (Tree BFS)
```text
Tree:
      1
     / \
    2   3
   / \   \
  4   5   6

Queue States:
Level 0: Queue = [1]
         Pop [1] -> Children [2, 3] added -> Queue = [2, 3] | Level List = [1]

Level 1: Queue = [2, 3] (size = 2)
         Pop [2] -> Children [4, 5] added -> Queue = [3, 4, 5]
         Pop [3] -> Child [6] added       -> Queue = [4, 5, 6] | Level List = [2, 3]

Level 2: Queue = [4, 5, 6] (size = 3)
         Pop [4], [5], [6] -> No children  -> Queue = []      | Level List = [4, 5, 6]
```

---

### 💻 Code Template (Tree BFS)
```javascript
function bfsTree(root) {
    if (!root) return [];
    
    const result = [];
    const queue = [root]; // Initialize queue with root

    while (queue.length > 0) {
        const levelSize = queue.length; // Capture number of nodes in current level
        const currentLevel = [];

        for (let i = 0; i < levelSize; i++) {
            const currentNode = queue.shift(); // Dequeue
            currentLevel.push(currentNode.val);

            // Enqueue left and right children
            if (currentNode.left) queue.push(currentNode.left);
            if (currentNode.right) queue.push(currentNode.right);
        }
        result.push(currentLevel); // Store current level nodes
    }
    return result;
}
```

---

## 🌲 Stack/Recursion Path Analysis (DFS)

### Concept:
DFS explores as deep as possible down a single branch before backtracking up to explore alternatives. It uses the call stack (recursion) or an explicit **Stack** (Last-In, First-Out) structure. It is optimal for evaluating paths (e.g. root-to-leaf paths) or checking connections.

### 💻 Code Template (Leaf-to-Root Path Tracking DFS)
```javascript
function findPaths(root, targetSum) {
    const allPaths = [];
    dfs(root, targetSum, [], allPaths);
    return allPaths;
}

function dfs(node, sum, currentPath, allPaths) {
    if (!node) return;

    // 1. Add current node to path
    currentPath.push(node.val);

    // 2. Check if current node is a leaf and meets target condition
    if (!node.left && !node.right && node.val === sum) {
        allPaths.push([...currentPath]); // Clone path
    } else {
        // 3. Traverse subtrees with remaining sum
        dfs(node.left, sum - node.val, currentPath, allPaths);
        dfs(node.right, sum - node.val, currentPath, allPaths);
    }

    // 4. Backtrack: remove current node from path before returning
    currentPath.pop();
}
```

---

## 🛠️ Graph Dependency Scheduling: Topological Sort

### Concept:
Topological Sort is used to find a linear ordering of vertices in a **Directed Acyclic Graph (DAG)** such that for every directed edge $u \rightarrow v$, vertex $u$ comes before $v$ in the ordering. This is the foundation of scheduling tasks (e.g. package installations, compiler build dependencies).

We implement Topological Sort using **Kahn's Algorithm** (BFS-based using In-degrees):

### 📐 ASCII Visualization (DAG with 4 Courses)
```text
Edges: [0 -> 1], [0 -> 2], [1 -> 3], [2 -> 3]

Graph layout:
     0
    / \
   v   v
   1   2
    \ /
     v
     3

1. Calculate in-degrees (number of incoming edges):
   In-degree: {0: 0, 1: 1, 2: 1, 3: 2}

2. Initialize Queue with 0-in-degree nodes: Queue = [0]
3. Dequeue 0: Add to order. Decrement children (1, 2) in-degrees.
   In-degree: {1: 0, 2: 0, 3: 2}
   Queue: [1, 2]
4. Dequeue 1: Add to order. Decrement child (3) in-degree.
   Queue: [2]
5. Dequeue 2: Add to order. Decrement child (3) in-degree. In-degree of 3 drops to 0!
   Queue: [3]
6. Dequeue 3: Add to order.
7. Final Order: [0, 1, 2, 3]
```

---

### 💻 Code Template (Kahn's Algorithm)
```javascript
function topologicalSort(numCourses, prerequisites) {
    const adjList = Array(numCourses).fill(0).map(() => []);
    const inDegree = Array(numCourses).fill(0);
    const order = [];

    // 1. Build Adjacency List and Calculate In-degrees
    for (let [course, pre] of prerequisites) {
        adjList[pre].push(course); // pre -> course
        inDegree[course]++;
    }

    // 2. Queue all vertices with 0 in-degree
    const queue = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) queue.push(i);
    }

    // 3. Process BFS queue
    while (queue.length > 0) {
        const u = queue.shift();
        order.push(u);

        for (let v of adjList[u]) {
            inDegree[v]--; // Decrement in-degree of neighbors
            if (inDegree[v] === 0) {
                queue.push(v);
            }
        }
    }

    // 4. Cycle Check: If order contains all nodes, sorting succeeded
    return order.length === numCourses ? order : [];
}
```
*   **Complexity:**
    *   Time Complexity: $O(V + E)$ where $V$ is vertices and $E$ is edges.
    *   Space Complexity: $O(V + E)$ to store the adjacency list.
