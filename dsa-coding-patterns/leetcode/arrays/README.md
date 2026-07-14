# Array Coding Problems

This directory tracks solutions and notes for array-based coding problems, primarily following Striver's A-Z DSA / Arrays Playlist.

Playlist: [Striver's Arrays Playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB)

> [!IMPORTANT]
> **Interactive Practice Protocol:**
> - **AI Role**: Design comprehensive test suites and stub out implementation files (without providing solution code upfront). Validate, run tests, analyze time/space complexity, and provide constructive code review feedback on User submissions.
> - **User Role**: Implement the solution in the corresponding Python file.

---

## 📚 Problems Index

| Problem | Difficulty | Status | Solution File |
| :--- | :--- | :--- | :--- |
| **1. Largest Element in an Array** | Easy | Completed (7/7 tests passed) | [largest_element.py](./largest_element.py) |
| **2. Second Largest Element in an Array** | Easy/Medium | Completed (9/9 tests passed) | [second_largest.py](./second_largest.py) |
| **3. Check if Array is Sorted** | Easy | Completed (9/9 tests passed) | [is_sorted.py](./is_sorted.py) |
| **4. Remove Duplicates from Sorted Array** | Easy | Completed (7/7 tests passed) | [remove_duplicates.py](./remove_duplicates.py) |

---

### 1. Largest Element in an Array
*   **Video Link:** [Video Tutorial (14/07/2026)](https://www.youtube.com/watch?v=37E9ckMDdTk&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=1&t=4s)
*   **Implementation:** [largest_element.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/largest_element.py)
*   **Difficulty:** Easy

#### 💡 Problem Statement
Given an array `arr` of size `N`, find the largest element in the array.

#### 📐 ASCII Visualization (Linear Scan)
```text
Array: [ 3,  2,  1,  5,  2 ]
Index:   0   1   2   3   4

Step 1: Initialize max = arr[0] = 3
[ 3,  2,  1,  5,  2 ]  => max = 3
  ^
 max

Step 2: Compare arr[1] (2) with max (3) -> 2 < 3 (No change)
[ 3,  2,  1,  5,  2 ]  => max = 3
      ^

Step 3: Compare arr[2] (1) with max (3) -> 1 < 3 (No change)
[ 3,  2,  1,  5,  2 ]  => max = 3
          ^

Step 4: Compare arr[3] (5) with max (3) -> 5 > 3 (Update max = 5)
[ 3,  2,  1,  5,  2 ]  => max = 5
              ^

Step 5: Compare arr[4] (2) with max (5) -> 2 < 5 (No change)
[ 3,  2,  1,  5,  2 ]  => max = 5
                  ^
Result: 5
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Sorting)
*   **Idea:** Sort the array in ascending order. The largest element will be at the last index (`arr[N-1]`).
*   **Time Complexity:** $O(N \log N)$ (due to sorting).
*   **Space Complexity:** $O(1)$ or $O(N)$ depending on the sorting algorithm.

##### 2. Optimal Approach (Linear Scan)
*   **Idea:** Scan the array from left to right, maintaining the maximum element seen so far.
*   **Time Complexity:** $O(N)$ (single pass traversal).
*   **Space Complexity:** $O(1)$ (no extra space).

#### 💻 Implementation (Python)
*Implement your solution directly in [largest_element.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/largest_element.py).*

---

### 2. Second Largest Element in an Array
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=37E9ckMDdTk&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=1&t=4s)
*   **Implementation:** [second_largest.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/second_largest.py)
*   **Difficulty:** Easy/Medium

#### 💡 Problem Statement
Given an array `arr` of size `N`, find the second largest element in the array. If the second largest element does not exist (e.g., all elements are identical, or the array has fewer than 2 elements), return `-1`.

#### 📐 ASCII Visualization (Optimal Single Pass)
```text
Array: [ 12, 35, 1, 10, 34, 1 ]
Index:    0   1  2   3   4  5

Step 1: Initialize largest = -1, second_largest = -1
[ 12, 35, 1, 10, 34, 1 ]
  ^
  arr[0] = 12 > largest (-1)
  => second_largest = largest = -1
  => largest = 12

Step 2: arr[1] = 35 > largest (12)
[ 12, 35, 1, 10, 34, 1 ]
      ^
  => second_largest = largest = 12
  => largest = 35

Step 3: arr[2] = 1 < second_largest (12) -> No change
[ 12, 35, 1, 10, 34, 1 ]
          ^

Step 4: arr[3] = 10 < second_largest (12) -> No change
[ 12, 35, 1, 10, 34, 1 ]
              ^

Step 5: arr[4] = 34. Since 34 < largest (35) AND 34 > second_largest (12):
[ 12, 35, 1, 10, 34, 1 ]
                  ^
  => second_largest = 34

Step 6: arr[5] = 1 < second_largest (34) -> No change

Result: 34
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Sorting)
*   **Idea:** Sort the array in descending order. Walk down from the start to find the first element that is strictly less than the largest element.
*   **Time Complexity:** $O(N \log N)$ (due to sorting).
*   **Space Complexity:** $O(1)$ or $O(N)$ depending on sorting algorithm.

##### 2. Better Approach (Two Passes)
*   **Idea:** In the first pass, find the largest element. In the second pass, find the largest element that is not equal to the largest element found in the first pass.
*   **Time Complexity:** $O(N)$ (two linear passes).
*   **Space Complexity:** $O(1)$ (no extra space).

##### 3. Optimal Approach (Single Pass)
*   **Idea:** Keep track of both `largest` and `second_largest` elements during a single traversal. For each element `x`, compare and update both values accordingly.
*   **Time Complexity:** $O(N)$ (single traversal).
*   **Space Complexity:** $O(1)$ (no extra space).

#### 💻 Implementation (Python)
*Implement your solution directly in [second_largest.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/second_largest.py).*

---

### 3. Check if Array is Sorted
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=37E9ckMDdTk&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=1&t=4s)
*   **Implementation:** [is_sorted.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/is_sorted.py)
*   **Difficulty:** Easy

#### 💡 Problem Statement
Given an array `arr` of size `N`, check if the array is sorted in non-decreasing (ascending) order. Return `True` if it is sorted, and `False` otherwise.

#### 📐 ASCII Visualization (Linear Scan)
```text
Sorted Array: [ 1, 2, 2, 5 ]
Index:          0  1  2  3

Step 1: Check index 1 vs 0
[ 1, 2, 2, 5 ] => arr[1] (2) >= arr[0] (1) -> Valid
     ^

Step 2: Check index 2 vs 1
[ 1, 2, 2, 5 ] => arr[2] (2) >= arr[1] (2) -> Valid
        ^

Step 3: Check index 3 vs 2
[ 1, 2, 2, 5 ] => arr[3] (5) >= arr[2] (2) -> Valid
           ^

Result: True
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Double Loop)
*   **Idea:** For each element at index `i`, check if all subsequent elements are greater than or equal to it.
*   **Time Complexity:** $O(N^2)$.
*   **Space Complexity:** $O(1)$.

##### 2. Optimal Approach (Single Pass Scan)
*   **Idea:** Traverse the array from left to right. At each index `i` (from `1` to `N-1`), check if `arr[i] >= arr[i-1]`. If this condition is violated at any point, return `False`.
*   **Time Complexity:** $O(N)$ (single pass traversal).
*   **Space Complexity:** $O(1)$ (no extra space).

#### 💻 Implementation (Python)
*Implement your solution directly in [is_sorted.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/is_sorted.py).*

---

### 4. Remove Duplicates from Sorted Array
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=37E9ckMDdTk&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=1&t=4s)
*   **Implementation:** [remove_duplicates.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/remove_duplicates.py)
*   **Difficulty:** Easy

#### 💡 Problem Statement
Given an array `arr` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in the array (let's call it `k`).

The first `k` elements of `arr` must contain the unique elements in their original sorted order.

#### 📐 ASCII Visualization (Two Pointer Approach)
```text
Array: [ 1, 1, 2, 2, 3 ]
Index:   0  1  2  3  4

Step 1: Initialize i = 0 (tracks position of last unique element)
[ 1, 1, 2, 2, 3 ]
  ^
  i
  
Step 2: j = 1 scan. Since arr[1] (1) == arr[i] (1), do nothing.
[ 1, 1, 2, 2, 3 ]
  ^  ^
  i  j

Step 3: j = 2 scan. Since arr[2] (2) != arr[i] (1), increment i, then set arr[i] = arr[j].
[ 1, 2, 2, 2, 3 ]
     ^  ^
     i  j

Step 4: j = 3 scan. Since arr[3] (2) == arr[i] (2), do nothing.
[ 1, 2, 2, 2, 3 ]
     ^     ^
     i     j

Step 5: j = 4 scan. Since arr[4] (3) != arr[i] (2), increment i, then set arr[i] = arr[j].
[ 1, 2, 3, 2, 3 ]
        ^     ^
        i     j

Result: Return k = i + 1 = 3. Unique portion: [ 1, 2, 3 ]
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Using Set)
*   **Idea:** Insert all elements of the array into a Set (which naturally removes duplicates). Then, overwrite the first `k` elements of the array with the set contents.
*   **Time Complexity:** $O(N)$ (to insert and write back).
*   **Space Complexity:** $O(N)$ (to store elements in the set).

##### 2. Optimal Approach (Two Pointers)
*   **Idea:** Keep two pointers `i` and `j`. Pointer `i` represents the position of the last unique element found. Pointer `j` iterates through the list. Whenever `arr[j]` is different from `arr[i]`, we increment `i` and write `arr[j]` to `arr[i]`.
*   **Time Complexity:** $O(N)$ (single pass traversal).
*   **Space Complexity:** $O(1)$ (in-place modification, no extra memory).

#### 💻 Implementation (Python)
*Implement your solution directly in [remove_duplicates.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/remove_duplicates.py).*



