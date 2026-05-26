# Chapter 1: Sliding Window & Two Pointers

This chapter covers two of the most fundamental array/string optimization patterns. Both patterns optimize brute force nested-loop approaches ($O(N^2)$) to linear time complexity ($O(N)$) by maintaining window boundaries or moving index pointers.

---

## 🪟 1. The Sliding Window Pattern

### Concept:
The Sliding Window pattern is used to perform operations on contiguous subarrays or substrings. Instead of recalculating the entire range from scratch for each starting position, we "slide" a window across the data structure, adding new elements from the right and discarding elements from the left.

### 📐 ASCII Visualization (Fixed Window of Size $K = 3$)
```text
Array: [ 1,  3,  2,  6, -1,  4,  1 ]
Index:   0   1   2   3   4   5   6

Step 1: Calculate initial window (indices 0 to 2)
[ 1,  3,  2 ] 6, -1,  4,  1    => Sum = 1 + 3 + 2 = 6
  L       R

Step 2: Slide right by 1 index (Subtract index 0, Add index 3)
  1, [ 3,  2,  6 ] -1,  4,  1  => Sum = 6 - 1 + 6 = 11
       L       R

Step 3: Slide right by 1 index (Subtract index 1, Add index 4)
  1,  3, [ 2,  6, -1 ]  4,  1  => Sum = 11 - 3 + (-1) = 7
           L       R
```

---

### 💻 Code Template (Variable Size Window)
Use this standard template to solve variable-size window problems (e.g., longest substring with constraints, shortest subarray matching a sum).

```javascript
function variableSlidingWindow(arr, targetCondition) {
    let left = 0;
    let windowState = {}; // Can be a sum, hash map, or character count set
    let maxLength = 0; // or minLength = Infinity

    for (let right = 0; right < arr.length; right++) {
        // 1. Expand the window: Add right element to state
        const rightVal = arr[right];
        windowState[rightVal] = (windowState[rightVal] || 0) + 1;

        // 2. Shrink the window: Check if the current window violates the condition
        while (violatesCondition(windowState, targetCondition)) {
            const leftVal = arr[left];
            windowState[leftVal]--;
            if (windowState[leftVal] === 0) delete windowState[leftVal];
            left++; // Slide left boundary rightward
        }

        // 3. Update Result: Store current valid window statistics
        maxLength = Math.max(maxLength, right - left + 1);
    }
    return maxLength;
}
```

---

### 📚 Core Problems & Solutions

#### Problem 1: Maximum Sum Subarray of Size $K$ (Fixed Window)
*   **Problem:** Find the maximum sum of any contiguous subarray of size $K$.
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Single pass traversal.
    *   Space Complexity: $O(1)$ — Only a few tracker variables.
*   **Implementation:**
    ```javascript
    function maxSubarraySum(arr, k) {
        if (arr.length < k) return 0;

        let maxSum = 0;
        let windowSum = 0;

        // Establish first window
        for (let i = 0; i < k; i++) {
            windowSum += arr[i];
        }
        maxSum = windowSum;

        // Slide window across remainder of array
        for (let i = k; i < arr.length; i++) {
            windowSum += arr[i] - arr[i - k]; // Add right, remove left
            maxSum = Math.max(maxSum, windowSum);
        }

        return maxSum;
    }
    ```

#### Problem 2: Minimum Size Subarray Sum (Variable Window)
*   **Problem:** Given an array of positive integers and a target sum $S$, find the minimal length of a contiguous subarray of which the sum is $\ge S$. If no such subarray exists, return 0.
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Each element is visited at most twice (once by right, once by left).
    *   Space Complexity: $O(1)$ — Constant memory.
*   **Implementation:**
    ```javascript
    function minSubArrayLen(target, nums) {
        let left = 0;
        let windowSum = 0;
        let minLength = Infinity;

        for (let right = 0; right < nums.length; right++) {
            windowSum += nums[right]; // Expand window

            // Shrink window as much as possible while sum >= target
            while (windowSum >= target) {
                minLength = Math.min(minLength, right - left + 1);
                windowSum -= nums[left]; // Shrink from left
                left++;
            }
        }

        return minLength === Infinity ? 0 : minLength;
    }
    ```

---

## 👈👉 2. The Two Pointers Pattern

### Concept:
The Two Pointers pattern utilizes two indexes to traverse a linear data structure simultaneously. Usually, one pointer starts at the beginning (index 0) and the other starts at the end (index $N-1$). They move towards each other until they meet. This is highly effective when searching for element pairs in **sorted** arrays.

### 📐 ASCII Visualization (Finding Two Sum = 9)
```text
Sorted Array: [ 2,  3,  5,  7, 11, 15 ]
Index:          0   1   2   3   4   5

Step 1: Pointers at extreme ends
[ 2,  3,  5,  7, 11, 15 ] => Sum = 2 + 15 = 17 (Greater than 9 -> Move R left)
  L                   R

Step 2: Decrement Right pointer
[ 2,  3,  5,  7, 11, 15 ] => Sum = 2 + 11 = 13 (Greater than 9 -> Move R left)
  L               R

Step 3: Decrement Right pointer
[ 2,  3,  5,  7, 11, 15 ] => Sum = 2 + 7 = 9 (Match found!)
  L           R
```

---

### 💻 Code Template (Opposite Direction Pointers)
```javascript
function oppositePointers(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        const sum = arr[left] + arr[right];
        if (sum === target) {
            return [left, right];
        } else if (sum < target) {
            left++; // Need larger values
        } else {
            right--; // Need smaller values
        }
    }
    return [-1, -1];
}
```

---

### 📚 Core Problems & Solutions

#### Problem 1: Two Sum in a Sorted Array
*   **Problem:** Find two numbers in a sorted array that add up to a target value.
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Linear scan.
    *   Space Complexity: $O(1)$ — No extra space.
*   **Implementation:** See Code Template above.

#### Problem 2: 3Sum (Target Sum to 0)
*   **Problem:** Given an integer array, return all unique triplets `[nums[i], nums[j], nums[k]]` such that $i \neq j, i \neq k$, and $j \neq k$, and `nums[i] + nums[j] + nums[k] === 0`.
*   **Complexity:**
    *   Time Complexity: $O(N^2)$ — Nested iteration (outer loop for first element, inner Two Pointers search).
    *   Space Complexity: $O(\log N)$ or $O(N)$ depending on sorting algorithm storage.
*   **Implementation:**
    ```javascript
    function threeSum(nums) {
        nums.sort((a, b) => a - b); // Sorting is mandatory
        const triplets = [];

        for (let i = 0; i < nums.length - 2; i++) {
            // Avoid duplicate outer values
            if (i > 0 && nums[i] === nums[i - 1]) continue;

            let left = i + 1;
            let right = nums.length - 1;

            while (left < right) {
                const sum = nums[i] + nums[left] + nums[right];

                if (sum === 0) {
                    triplets.push([nums[i], nums[left], nums[right]]);
                    
                    // Skip duplicates for left & right pointers
                    while (left < right && nums[left] === nums[left + 1]) left++;
                    while (left < right && nums[right] === nums[right - 1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return triplets;
    }
    ```
