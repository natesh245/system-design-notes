# Chapter 6: Monotonic Stack & Backtracking

This chapter covers two algorithmic patterns: **Monotonic Stack** (used to resolve "nearest greater/smaller element" queries in linear time) and **Backtracking** (a DFS-based recursion pattern used to systematically search a solution space to generate all combinations, subsets, or permutations).

---

## 🗄️ 1. The Monotonic Stack Pattern

### Concept:
A Monotonic Stack is a stack that maintains elements in a strict sorting order (either monotonically increasing or decreasing).
*   **Monotonic Decreasing Stack:** Elements are stored from largest to smallest. If we encounter a new element that is *larger* than the stack's top element, we repeatedly pop from the stack until we can push the new element.
*   **Why it's fast:** Each element in the array is pushed onto the stack exactly once and popped at most once, resulting in a **$O(N)$** execution time instead of nested-loop $O(N^2)$ solutions.

### 📐 ASCII Visualization (Next Greater Element)
```text
Array: [ 2,  1,  2,  4,  3 ]
Index:   0   1   2   3   4

1. i = 0 (val = 2): Stack is empty. Push index 0.
   Stack = [0] (representing value 2)

2. i = 1 (val = 1): 1 is NOT greater than Stack top (val = 2). Push index 1.
   Stack = [0, 1] (representing values 2, 1)

3. i = 2 (val = 2): 2 IS greater than Stack top index 1 (val = 1).
   Pop index 1 -> Result[1] = 2.
   Stack = [0]. Now, 2 is NOT greater than Stack top index 0 (val = 2). Push index 2.
   Stack = [0, 2] (representing values 2, 2)

4. i = 3 (val = 4): 4 IS greater than Stack top index 2 (val = 2).
   Pop index 2 -> Result[2] = 4.
   Stack = [0]. 4 IS greater than Stack top index 0 (val = 2).
   Pop index 0 -> Result[0] = 4.
   Stack = []. Push index 3.
   Stack = [3] (representing value 4)

5. i = 4 (val = 3): 3 is NOT greater than Stack top index 3 (val = 4). Push index 4.
   Stack = [3, 4]
```

---

### 💻 Code Template (Next Greater Element)
```javascript
function nextGreaterElement(nums) {
    const result = Array(nums.length).fill(-1);
    const stack = []; // Store indices of elements

    for (let i = 0; i < nums.length; i++) {
        // While stack has items and current element is larger than value at stack's top index
        while (stack.length > 0 && nums[i] > nums[stack[stack.length - 1]]) {
            const poppedIndex = stack.pop();
            result[poppedIndex] = nums[i]; // Store next greater element
        }
        stack.push(i); // Push current index
    }
    return result;
}
```

---

### 📚 Core Problems & Solutions

#### Problem 1: Daily Temperatures
*   **Problem:** Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the $i$-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Linear scan.
    *   Space Complexity: $O(N)$ — Stack storage.
*   **Implementation:**
    ```javascript
    function dailyTemperatures(temperatures) {
        const n = temperatures.length;
        const result = Array(n).fill(0);
        const stack = []; // Stores indices

        for (let i = 0; i < n; i++) {
            while (stack.length > 0 && temperatures[i] > temperatures[stack[stack.length - 1]]) {
                const prevIdx = stack.pop();
                result[prevIdx] = i - prevIdx; // Calculate day difference
            }
            stack.push(i);
        }
        return result;
    }
    ```

---

## 🔀 2. The Backtracking Pattern

### Concept:
Backtracking is an algorithmic-technique that builds candidates for a solution incrementally, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly lead to a valid solution.

### 📐 Decision Tree Visualization (Subsets of `[1, 2]`)
```text
                     [ ] (Start)
                    /   \
                Add 1    Skip 1
                 /         \
              [1]          [ ]
             /   \        /   \
          Add 2  Skip 2 Add 2 Skip 2
           /       \     /      \
        [1,2]     [1]   [2]     [ ]
```

---

### 💻 Code Templates

#### A. Subsets Template
```javascript
function subsets(nums) {
    const list = [];
    nums.sort((a, b) => a - b); // Sorting handles duplicates if needed
    backtrackSubsets(list, [], nums, 0);
    return list;
}

function backtrackSubsets(list, tempList, nums, start) {
    list.push([...tempList]); // Add deep copy of current state
    for (let i = start; i < nums.length; i++) {
        tempList.push(nums[i]); // 1. Make choice
        backtrackSubsets(list, tempList, nums, i + 1); // 2. Recurse
        tempList.pop(); // 3. Undo choice (Backtrack)
    }
}
```

#### B. Permutations Template
```javascript
function permute(nums) {
    const list = [];
    backtrackPermute(list, [], nums, new Set());
    return list;
}

function backtrackPermute(list, tempList, nums, used) {
    if (tempList.length === nums.length) {
        list.push([...tempList]);
        return;
    }
    for (let i = 0; i < nums.length; i++) {
        if (used.has(nums[i])) continue; // Element is already in the permutation

        tempList.push(nums[i]); // Make choice
        used.add(nums[i]);
        
        backtrackPermute(list, tempList, nums, used); // Recurse
        
        used.delete(nums[i]); // Undo choice (Backtrack)
        tempList.pop();
    }
}
```
*   **Complexity (Permutations):**
    *   Time Complexity: $O(N \cdot N!)$ — There are $N!$ permutations, and creating a copy of each takes $O(N)$ time.
    *   Space Complexity: $O(N)$ — Deepest recursion tree call stack and `used` Set size.
