# Chapter 7: Dynamic Programming

Dynamic Programming (DP) optimizes plain recursion by solving each subproblem exactly once and caching the result. In senior backend interviews, you are expected to know the two core conditions for DP (Overlapping Subproblems and Optimal Substructure) and be comfortable transitioning from **Top-Down (Memoization)** to **Bottom-Up (Tabulation)** solutions.

---

## 🆚 Memoization vs. Tabulation

| Metric | Top-Down (Memoization) | Bottom-Up (Tabulation) |
| :--- | :--- | :--- |
| **Execution** | Starts from the main problem, solves subproblems recursively as needed, and stores results in a lookup table (e.g. Map/Array). | Starts from the base cases (smallest subproblems), iterates up to the target problem, and fills a table (1D/2D Array) sequentially. |
| **Complexity** | Easy to conceptualize from brute-force recursion. Has overhead due to recursion stack frames. | Highly memory efficient; eliminates recursion stack frame overhead and enables space optimizations. |

---

## 🎒 1. The 0/1 Knapsack Pattern

### Concept:
Given $N$ items, each with a weight $W[i]$ and a value $V[i]$, and a knapsack of capacity $C$. We want to find the maximum value we can fit in the knapsack. Each item can either be taken (1) or left (0).

### State Transition:
For item $i$ and capacity $c$:
$$\text{DP}[i][c] = \max(\text{DP}[i-1][c], \text{Value}[i] + \text{DP}[i-1][c - \text{Weight}[i]])$$

*   **Exclude item:** Take the max value from the previous $i-1$ items at same capacity $c$.
*   **Include item:** Add current item value to the max value of previous $i-1$ items with capacity reduced by the current item's weight.

---

### 💻 Code Solution (Tabulation with Space Optimization)
*   **Complexity:**
    *   Time Complexity: $O(N \cdot C)$ where $N$ is the number of items and $C$ is the knapsack capacity.
    *   Space Complexity: $O(C)$ — Optimized from $O(N \cdot C)$ by only tracking the previous row.
*   **Implementation:**
    ```javascript
    function solveKnapsack(values, weights, capacity) {
        const n = values.length;
        if (capacity <= 0 || n === 0 || weights.length !== n) return 0;

        // DP array of size capacity + 1 (stores max value for each capacity)
        const dp = Array(capacity + 1).fill(0);

        // Process first item
        for (let c = 0; c <= capacity; c++) {
            if (weights[0] <= c) dp[c] = values[0];
        }

        // Process remaining items
        for (let i = 1; i < n; i++) {
            // Traverse backwards to prevent using the same item multiple times in one iteration
            for (let c = capacity; c >= 0; c--) {
                if (weights[i] <= c) {
                    dp[c] = Math.max(dp[c], values[i] + dp[c - weights[i]]);
                }
            }
        }

        return dp[capacity];
    }
    ```

---

## 🔀 2. Longest Common Subsequence (LCS)

### Concept:
Given two strings $S1$ and $S2$, find the length of their longest common subsequence (a subsequence is a sequence that appears in the same relative order, but not necessarily contiguously).

### State Transition:
*   If characters match ($S1[i] === S2[j]$):
    $$\text{DP}[i][j] = 1 + \text{DP}[i-1][j-1]$$
*   If they do not match:
    $$\text{DP}[i][j] = \max(\text{DP}[i-1][j], \text{DP}[i][j-1])$$

---

### 💻 Code Solution (Bottom-Up Tabulation)
*   **Complexity:**
    *   Time Complexity: $O(M \cdot N)$ where $M$ and $N$ are the lengths of both strings.
    *   Space Complexity: $O(M \cdot N)$ — 2D table grid.
*   **Implementation:**
    ```javascript
    function longestCommonSubsequence(text1, text2) {
        const m = text1.length;
        const n = text2.length;
        
        // 2D DP array initialized to 0
        const dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

        for (let i = 1; i <= m; i++) {
            for (let j = 1; j <= n; j++) {
                if (text1[i - 1] === text2[j - 1]) {
                    // Match found: Increment count from diagonal cell
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    // No match: Take max from top or left cell
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[m][n];
    }
    ```

---

## 📈 3. Longest Increasing Subsequence (LIS)

### Concept:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

### State Transition:
For each element $i$, compare it with all elements $j$ that come before it ($j < i$):
*   If $nums[i] > nums[j]$:
    $$\text{DP}[i] = \max(\text{DP}[i], 1 + \text{DP}[j])$$

---

### 💻 Code Solutions

#### Option A: Bottom-Up Dynamic Programming
*   **Complexity:**
    *   Time Complexity: $O(N^2)$ — Nested iteration checking all preceding elements.
    *   Space Complexity: $O(N)$ — 1D tracking array.
*   **Implementation:**
    ```javascript
    function lengthOfLIS(nums) {
        if (nums.length === 0) return 0;

        const dp = Array(nums.length).fill(1); // Base case: every element is an LIS of length 1
        let maxLIS = 1;

        for (let i = 1; i < nums.length; i++) {
            for (let j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], 1 + dp[j]);
                }
            }
            maxLIS = Math.max(maxLIS, dp[i]);
        }

        return maxLIS;
    }
    ```

#### Option B: Binary Search Optimization (Patience Sorting)
For senior interviews, you may be asked to optimize LIS to $O(N \log N)$ using a greedy array combined with binary search.
*   **Complexity:**
    *   Time Complexity: $O(N \log N)$ — Binary search is performed for each of the $N$ elements.
    *   Space Complexity: $O(N)$ — Active subsequence array.
*   **Implementation:**
    ```javascript
    function lengthOfLISOptimized(nums) {
        const tails = []; // Stores the smallest tail of all increasing subsequences of different lengths

        for (let num of nums) {
            let left = 0;
            let right = tails.length;

            // Binary search to find index to insert/replace num in tails
            while (left < right) {
                const mid = Math.floor(left + (right - left) / 2);
                if (tails[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            // Replace or append
            tails[left] = num;
        }

        return tails.length;
    }
    ```
