# Chapter 3: Cyclic Sort & Modified Binary Search

This chapter covers two powerful array traversal patterns. **Cyclic Sort** solves missing/duplicate value problems in linear time ($O(N)$) and constant space ($O(1)$), while **Modified Binary Search** solves search problems in sorted, rotated, or peaked arrays in logarithmic time ($O(\log N)$).

---

## 🔄 1. The Cyclic Sort Pattern

### Concept:
This pattern is applied to arrays containing numbers in a defined range (e.g., $1 \dots N$ or $0 \dots N$). Instead of sorting the array using expensive algorithms ($O(N \log N)$), we iterate through the array and place each number at its "correct index" (number $X$ goes to index $X-1$). We do this by swapping elements.

### 📐 ASCII Visualization (Sorting numbers $1 \dots 5$)
```text
Array: [ 3,  1,  5,  4,  2 ]
Index:   0   1   2   3   4

Step 1: Inspect index 0 (val = 3). Correct index for 3 is 3-1 = 2.
Swap index 0 and 2.
[ 5,  1,  3,  4,  2 ]
  ^       ^

Step 2: Inspect index 0 (val = 5). Correct index for 5 is 5-1 = 4.
Swap index 0 and 4.
[ 2,  1,  3,  4,  5 ]
  ^               ^

Step 3: Inspect index 0 (val = 2). Correct index for 2 is 2-1 = 1.
Swap index 0 and 1.
[ 1,  2,  3,  4,  5 ]
  ^   ^

Step 4: Inspect index 0 (val = 1). Matches index 0. Increment index.
Step 5: Inspect index 1 (val = 2). Matches index 1. Increment index.
... Array is fully sorted in 4 swaps!
```

---

### 💻 Code Template (Range $1 \dots N$)
```javascript
function cyclicSort(nums) {
    let i = 0;
    while (i < nums.length) {
        const correctIndex = nums[i] - 1; // Correct index for value nums[i]
        
        // Swap if element is not in its correct position
        if (nums[i] !== nums[correctIndex]) {
            [nums[i], nums[correctIndex]] = [nums[correctIndex], nums[i]];
        } else {
            i++; // Move to next element only when correct element is at index i
        }
    }
    return nums;
}
```

---

### 📚 Core Problems & Solutions

#### Problem 1: Find the Missing Number (Range $0 \dots N$)
*   **Problem:** Given an array containing $n$ distinct numbers in the range $[0, n]$, return the only number in the range that is missing from the array.
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Single scan sorting, then another scan to identify the missing index.
    *   Space Complexity: $O(1)$ — In-place array modification.
*   **Implementation:**
    ```javascript
    function missingNumber(nums) {
        let i = 0;
        const n = nums.length;

        // Cyclic sort for range 0 to N
        while (i < n) {
            const correctIndex = nums[i];
            
            // If value is less than N and not at correct index, swap
            if (nums[i] < n && nums[i] !== nums[correctIndex]) {
                [nums[i], nums[correctIndex]] = [nums[correctIndex], nums[i]];
            } else {
                i++;
            }
        }

        // Find the index containing the wrong number
        for (let j = 0; j < n; j++) {
            if (nums[j] !== j) return j;
        }

        return n; // If 0 to N-1 are correct, N is missing
    }
    ```

#### Problem 2: Find the Duplicate Number
*   **Problem:** Given an array of integers `nums` containing $n + 1$ integers where each integer is in the range $[1, n]$ inclusive, return the duplicate number. Do not modify the array's values (read-only) or use extra space. (We can use Cyclic Sort if we can temporarily modify array, or Floyd's cycle detection. Here is the Cyclic Sort implementation).
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Linear search.
    *   Space Complexity: $O(1)$ — Constant memory.
*   **Implementation:**
    ```javascript
    function findDuplicate(nums) {
        let i = 0;
        while (i < nums.length) {
            if (nums[i] !== i + 1) {
                const correctIndex = nums[i] - 1;
                
                // If the target position already has the correct number, we found the duplicate!
                if (nums[i] !== nums[correctIndex]) {
                    [nums[i], nums[correctIndex]] = [nums[correctIndex], nums[i]];
                } else {
                    return nums[i];
                }
            } else {
                i++;
            }
        }
        return -1;
    }
    ```

---

## 🔍 2. Modified Binary Search Pattern

### Concept:
Standard Binary Search operates on a fully sorted array by repeatedly dividing the search space in half. **Modified Binary Search** extends this to handle partially sorted arrays (e.g., rotated arrays) or search conditions that change dynamically (e.g., finding boundaries or peaks).

### 📐 ASCII Visualization (Rotated Array Search)
```text
Rotated Sorted Array: [ 4,  5,  6,  7,  0,  1,  2 ]   Target = 0
Index:                  0   1   2   3   4   5   6

Step 1: Check boundaries and mid
L = 0 (4), R = 6 (2), Mid = 3 (7)
[ 4,  5,  6,  (7),  0,  1,  2 ]  => Left half (4 to 7) is sorted!
  L           M             R

Is Target (0) in the sorted range [4, 7]? No.
So, search in right half: L = Mid + 1 = 4.

Step 2: Update pointers
L = 4 (0), R = 6 (2), Mid = 5 (1)
[ 4,  5,  6,  7,  (0),  1,  2 ] => Match found at index 4!
                   L    M   R
```

---

### 💻 Code Template (Search in Rotated Sorted Array)
```javascript
function searchRotated(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);

        if (nums[mid] === target) return mid;

        // 1. Determine which half is sorted
        if (nums[left] <= nums[mid]) {
            // Left half is sorted
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1; // Search left
            } else {
                left = mid + 1; // Search right
            }
        } else {
            // Right half is sorted
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1; // Search right
            } else {
                right = mid - 1; // Search left
            }
        }
    }
    return -1;
}
```

---

### 📚 Core Problems & Solutions

#### Problem 1: Find Peak Element
*   **Problem:** A peak element is an element that is strictly greater than its neighbors. Find the index of a peak element in an array.
*   **Complexity:**
    *   Time Complexity: $O(\log N)$ — Binary search.
    *   Space Complexity: $O(1)$ — No extra space.
*   **Implementation:**
    ```javascript
    function findPeakElement(nums) {
        let left = 0;
        let right = nums.length - 1;

        while (left < right) {
            const mid = Math.floor(left + (right - left) / 2);
            
            // If mid element is smaller than its right neighbor, 
            // the peak must lie on the right side.
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                // Otherwise, peak lies on the left side (including mid).
                right = mid;
            }
        }
        return left; // left and right meet at a peak
    }
    ```
