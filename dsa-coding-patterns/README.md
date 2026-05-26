# Data Structures & Algorithms (DSA) Coding Patterns Guide

Welcome to the Data Structures & Algorithms preparation curriculum. Rather than memorizing hundreds of separate LeetCode questions, this roadmap focuses on **Coding Patterns**—the core algorithmic templates that can solve over 90% of backend engineering coding interviews.

---

## 🗺️ Curriculum Syllabus

Click on any module below to dive into the detailed conceptual explanations, ASCII visuals, complexity breakdowns, code templates, and LeetCode-style implementations.

| Module | Pattern Category | Key Topics & Algorithms |
| :--- | :--- | :--- |
| **01** | [Sliding Window & Two Pointers](./01-sliding-window-two-pointers.md) | Fixed/Variable Subarrays, Two Sum Sorted, 3Sum, Subarray Min/Max, Boundary Convergence. |
| **02** | [Fast & Slow Pointers, Merge Intervals](./02-fast-slow-pointers-intervals.md) | Linked List Cycle Detection, Midpoint Finding, Intersecting/Merging Intervals, Interval Insertion. |
| **03** | [Cyclic Sort & Modified Binary Search](./03-cyclic-sort-binary-search.md) | In-place Sorting of $1 \dots N$ ranges, Duplicate/Missing Number discovery, Rotated Sorted Array Search. |
| **04** | [Trees, Graphs, BFS & DFS](./04-trees-graphs-bfs-dfs.md) | Tree Traversals (Level/Zigzag), Path Sums, Topological Sort (Kahn's), Directed Graph Cycle Detection. |
| **05** | [Heaps & Top K Elements](./05-heaps-top-k-elements.md) | Min/Max Heaps, Top K largest, K-Way Merges, Dynamic Stream Median finding (Two Heaps pattern). |
| **06** | [Monotonic Stack & Backtracking](./06-monotonic-stack-backtracking.md) | Next Greater Element, Daily Temperatures, Permutations, Subsets, Combination Sum, Recursion. |
| **07** | [Dynamic Programming](./07-dynamic-programming.md) | Memoization/Tabulation, 0/1 Knapsack, Longest Common Subsequence, Longest Increasing Subsequence. |

---

## 🧠 Pattern Recognition Heuristics

During a live interview, use these rules of thumb to determine which pattern applies to the given problem:

| If the problem asks for: | ...and the input structure is: | **You should use: (The Pattern)** |
| :--- | :--- | :--- |
| Contiguous subarray matching a sum/limit/length constraint | Array, String, or Linked List | **Sliding Window** |
| Target sum/pairs in a sorted array, or reversing structures | Sorted Array, Linked List | **Two Pointers** |
| Finding a cycle or loop in a list, or list middle node | Linked List, Circular Array | **Fast & Slow Pointers** |
| Overlapping ranges, scheduling, calendar slots, merges | List of Pairs/Intervals | **Merge Intervals** |
| Finding missing/duplicate values in a sequence of $1 \dots N$ | Unsorted array of numbers | **Cyclic Sort** |
| Searching in a sorted array or list under $O(\log N)$ constraint | Sorted Array, Rotated Array | **Modified Binary Search** |
| Level-by-level traversal or shortest path in trees/graphs | Binary Tree, Graph, Matrix | **BFS (Breadth-First Search)** |
| All paths from root-to-leaf, or exploring deep branches | Binary Tree, Graph | **DFS (Depth-First Search)** |
| Scheduling dependencies, order-of-execution, DAGs | Directed Acyclic Graph (DAG) | **Topological Sort** |
| Top/Smallest/Largest $K$ items, or merging multiple sorted lists | Array, Stream | **Top K Elements / K-Way Merge** |
| Dynamic running median or splitting array into high/low parts | Stream of Numbers | **Two Heaps** |
| Finding next greater/smaller element in a sequence | Array (typically unsorted) | **Monotonic Stack** |
| Generating all combinations, permutations, or paths | Set of items | **Backtracking (Subsets)** |
| Finding optimal choices (min/max cost), subproblem overlap | Overlapping subproblems | **Dynamic Programming** |

---

## ⚡ Live Interview Strategy

When presented with a coding problem, follow this structured execution framework:

1.  **Clarify Requirements:** Ask questions to identify edge cases ($O$, null values, duplicates, size boundaries). State your assumptions.
2.  **Sketch Examples:** Walk through a simple input/output example by hand to verify your understanding.
3.  **Identify Pattern:** Look at the heuristics table above to match your problem to an algorithmic pattern.
4.  **Propose Brute Force First:** Briefly explain the obvious, simple approach and state its time/space complexity (e.g. $O(N^2)$).
5.  **Optimize using Pattern:** Explain how the matched pattern optimizes the time complexity (e.g., down to $O(N)$ or $O(N \log N)$).
6.  **Write Code:** Implement clean, modular code. Add input validation guards (e.g., null checks).
7.  **Dry Run:** Trace your code using a simple test case. Write out variable states step-by-step.
8.  **Analyze Complexity:** Clearly state the final Time and Space complexities using Big-O notation.
