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
| **5. Left Rotate an Array by One** | Easy | In Progress (0/6 tests passed) | [left_rotate_one.py](./left_rotate_one.py) |
| **6. Left Rotate an Array by d Places** | Easy/Medium | In Progress (0/7 tests passed) | [left_rotate_d.py](./left_rotate_d.py) |
| **7. Move Zeros to End** | Easy | In Progress (0/7 tests passed) | [move_zeros.py](./move_zeros.py) |
| **8. Linear Search** | Easy | Completed (7/7 tests passed) | [linear_search.py](./linear_search.py) |
| **9. Union of Two Sorted Arrays** | Easy/Medium | In Progress (0/7 tests passed) | [union_arrays.py](./union_arrays.py) |
| **10. Intersection of Two Sorted Arrays** | Easy/Medium | Completed (13/13 tests passed) | [intersection_arrays.py](./intersection_arrays.py) |

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

---

### 5. Left Rotate an Array by One
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=wvcQg43_V8M&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=12)
*   **Implementation:** [left_rotate_one.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/left_rotate_one.py)
*   **Difficulty:** Easy

#### 💡 Problem Statement
Given an array `arr` of size `N`, left rotate the array by one place (i.e. shift all elements to the left by one position, and move the first element to the last position). The modification should be done in-place.

#### 📐 ASCII Visualization (Left Rotation)
```text
Array: [ 1, 2, 3, 4, 5 ]
Index:   0  1  2  3  4

Step 1: Store the first element in a temporary variable.
temp = arr[0] = 1

Step 2: Shift all subsequent elements one position to the left.
arr[0] = arr[1]  => [ 2, 2, 3, 4, 5 ]
arr[1] = arr[2]  => [ 2, 3, 3, 4, 5 ]
arr[2] = arr[3]  => [ 2, 3, 4, 4, 5 ]
arr[3] = arr[4]  => [ 2, 3, 4, 5, 5 ]

Step 3: Place temp at the last index.
arr[4] = temp    => [ 2, 3, 4, 5, 1 ]

Result: [ 2, 3, 4, 5, 1 ]
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Using Auxiliary Array)
*   **Idea:** Create a new array of size `N`. Copy `arr[1...N-1]` to the new array at index `0...N-2`, and copy `arr[0]` to the last index.
*   **Time Complexity:** $O(N)$
*   **Space Complexity:** $O(N)$ (to store the rotated array).

##### 2. Optimal Approach (In-place Shifting)
*   **Idea:** Save `arr[0]` in a variable `temp`. Shift elements from index `1` to `N-1` one position to the left. Then place `temp` at `arr[N-1]`.
*   **Time Complexity:** $O(N)$ (single pass traversal).
*   **Space Complexity:** $O(1)$ (no extra space, done in-place).

#### 💻 Implementation (Python)
*Implement your solution directly in [left_rotate_one.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/left_rotate_one.py).*

---

### 6. Left Rotate an Array by d Places
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=wvcQg43_V8M&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=12)
*   **Implementation:** [left_rotate_d.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/left_rotate_d.py)
*   **Difficulty:** Easy/Medium

#### 💡 Problem Statement
Given an array `arr` of size `N` and a non-negative integer `d`, left rotate the array by `d` places (i.e. shift all elements to the left by `d` positions, wrapping the first `d` elements around to the end). The modification should be done in-place.

#### 📐 ASCII Visualization (Reversal Algorithm)
Assume `arr = [1, 2, 3, 4, 5, 6, 7]`, `d = 3`.
`N = 7`. Since `d = 3`, we do `d = d % N = 3 % 7 = 3`.

```text
Original: [ 1, 2, 3, 4, 5, 6, 7 ]

Step 1: Reverse first d elements: arr[0...d-1] (indices 0 to 2)
[ 3, 2, 1, 4, 5, 6, 7 ]
  <----->

Step 2: Reverse remaining N-d elements: arr[d...N-1] (indices 3 to 6)
[ 3, 2, 1, 7, 6, 5, 4 ]
           <---------->

Step 3: Reverse the entire array: arr[0...N-1] (indices 0 to 6)
[ 4, 5, 6, 7, 1, 2, 3 ]
  <------------------->

Result: [ 4, 5, 6, 7, 1, 2, 3 ]
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Using Auxiliary Array)
*   **Idea:** Copy the first `d` elements to a temporary array. Shift the remaining `N-d` elements to the left. Copy the `d` elements back to the end of the original array.
*   **Time Complexity:** $O(N)$
*   **Space Complexity:** $O(d)$ (to store the temporary elements).

##### 2. Optimal Approach (Reversal Algorithm)
*   **Idea:** Reverse the first `d` elements. Reverse the remaining `N-d` elements. Reverse the entire array.
*   **Time Complexity:** $O(N)$ (as each element is reversed twice).
*   **Space Complexity:** $O(1)$ (no extra space, done in-place).

#### 💻 Implementation (Python)
*Implement your solution directly in [left_rotate_d.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/left_rotate_d.py).*

---

### 7. Move Zeros to End
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=wvcQg43_V8M&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=12)
*   **Implementation:** [move_zeros.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/move_zeros.py)
*   **Difficulty:** Easy

#### 💡 Problem Statement
Given an array `arr` of size `N`, move all zeros in the array to the end while maintaining the relative order of the non-zero elements. The modification must be done in-place.

#### 📐 ASCII Visualization (Two Pointer Swap)
Assume `arr = [ 1, 0, 2, 3, 0, 4 ]`.
Find first zero at index 1: `j = 1`.
Start `i = j + 1 = 2` to scan the rest of the array.

```text
Step 1: arr[2] = 2. Since arr[2] != 0, swap arr[i] (2) and arr[j] (0). Increment j to point to the next zero.
[ 1, 2, 0, 3, 0, 4 ]
     ^  ^
     j  i

Step 2: arr[3] = 3. Since arr[3] != 0, swap arr[i] (3) and arr[j] (0). Increment j.
[ 1, 2, 3, 0, 0, 4 ]
        ^  ^
        j  i

Step 3: arr[4] = 0. Since arr[4] == 0, do nothing.
[ 1, 2, 3, 0, 0, 4 ]
        ^     ^
        j     i

Step 4: arr[5] = 4. Since arr[5] != 0, swap arr[i] (4) and arr[j] (0). Increment j.
[ 1, 2, 3, 4, 0, 0 ]
           ^     ^
           j     i

Result: [ 1, 2, 3, 4, 0, 0 ]
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Using Temporary Array)
*   **Idea:** Create a temporary array. Traverse `arr` and copy all non-zero elements to the temp array. Then, fill the remaining spots in temp with zeros. Copy temp back to `arr`.
*   **Time Complexity:** $O(N)$
*   **Space Complexity:** $O(N)$ (requires auxiliary space for all elements).

##### 2. Optimal Approach (Two Pointers)
*   **Idea:** Find the first zero index `j`. Traverse index `i` from `j+1` to `N-1`. Whenever `arr[i]` is non-zero, swap `arr[i]` and `arr[j]`, then increment `j`.
*   **Time Complexity:** $O(N)$ (single pass traversal).
*   **Space Complexity:** $O(1)$ (no extra space, done in-place).

#### 💻 Implementation (Python)
*Implement your solution directly in [move_zeros.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/move_zeros.py).*

---

### 8. Linear Search
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=37E9ckMDdTk&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=1&t=4s)
*   **Implementation:** [linear_search.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/linear_search.py)
*   **Difficulty:** Easy

#### 💡 Problem Statement
Given an array `arr` and a target element `num`, find the index of the first occurrence of `num` in the array. If the element is not found, return `-1`.

#### 📐 ASCII Visualization (Sequential Iteration)
Assume `arr = [ 5, 4, 3, 2, 1 ]`, `num = 3`.

```text
Step 1: Check index 0. arr[0] = 5 != 3
[ 5, 4, 3, 2, 1 ]
  ^

Step 2: Check index 1. arr[1] = 4 != 3
[ 5, 4, 3, 2, 1 ]
     ^

Step 3: Check index 2. arr[2] = 3 == 3. Found! Return 2.
[ 5, 4, 3, 2, 1 ]
        ^

Result: 2
```

#### ⚙️ Approaches & Complexity

##### 1. Optimal Approach (Sequential Iteration)
*   **Idea:** Iterate through the array sequentially from index `0` to `N-1`. If an element equals `num`, return its index immediately. If the loop completes without finding `num`, return `-1`.
*   **Time Complexity:** $O(N)$ (in the worst case, we scan the entire array).
*   **Space Complexity:** $O(1)$ (no extra memory is allocated).

#### 💻 Implementation (Python)
*Implement your solution directly in [linear_search.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/linear_search.py).*

---

### 9. Union of Two Sorted Arrays
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=wvcQg43_V8M&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=12)
*   **Implementation:** [union_arrays.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/union_arrays.py)
*   **Difficulty:** Easy/Medium

#### 💡 Problem Statement
Given two sorted arrays `arr1` and `arr2`, find the union of these two arrays. The union array should contain only unique elements, sorted in ascending order.

#### 📐 ASCII Visualization (Two Pointer Comparison)
Assume `arr1 = [ 1, 1, 2, 3, 4 ]` and `arr2 = [ 2, 3, 5, 6 ]`.
Set pointers `i = 0` (points to `arr1`), `j = 0` (points to `arr2`).

```text
Step 1: arr1[i] = 1, arr2[j] = 2. Since 1 < 2, add 1 to union. Increment i.
union: [ 1 ]
   arr1: [ 1, 1, 2, 3, 4 ]   arr2: [ 2, 3, 5, 6 ]
             ^                         ^
             i                         j

Step 2: arr1[i] = 1, arr2[j] = 2. Since 1 < 2, we check if 1 is already in union. It is, so skip duplicate. Increment i.
union: [ 1 ]
   arr1: [ 1, 1, 2, 3, 4 ]   arr2: [ 2, 3, 5, 6 ]
                ^                      ^
                i                      j

Step 3: arr1[i] = 2, arr2[j] = 2. They are equal. Add 2 to union (2 != union[-1]). Increment both i and j.
union: [ 1, 2 ]
   arr1: [ 1, 1, 2, 3, 4 ]   arr2: [ 2, 3, 5, 6 ]
                   ^                      ^
                   i                      j

Step 4: arr1[i] = 3, arr2[j] = 3. They are equal. Add 3 to union (3 != union[-1]). Increment both.
union: [ 1, 2, 3 ]
   arr1: [ 1, 1, 2, 3, 4 ]   arr2: [ 2, 3, 5, 6 ]
                      ^                      ^
                      i                      j

Step 5: arr1[i] = 4, arr2[j] = 5. Since 4 < 5, add 4 to union. Increment i.
union: [ 1, 2, 3, 4 ]
   arr1: [ 1, 1, 2, 3, 4 ]   arr2: [ 2, 3, 5, 6 ]
                         ^                   ^
                        (end)                j

Step 6: arr1 is exhausted. Process remaining elements in arr2: Add 5 then 6 (checking duplicates).
Result: [ 1, 2, 3, 4, 5, 6 ]
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Using Set)
*   **Idea:** Insert all elements of `arr1` and `arr2` into a Set (which handles ordering/uniqueness in tree-based sets, or we sort the final list if using hash-sets).
*   **Time Complexity:** $O((N+M) \log(N+M))$ if we insert all elements and sort, or $O(N+M)$ using hash sets + sorting of size $U$ (where $U$ is the number of unique elements).
*   **Space Complexity:** $O(N+M)$ to store the set.

##### 2. Optimal Approach (Two Pointers)
*   **Idea:** Since both arrays are already sorted, use a two-pointer approach comparing the current elements of both arrays. Keep track of the last added element to prevent duplicates in the union list.
*   **Time Complexity:** $O(N + M)$ (single pass through both arrays).
*   **Space Complexity:** $O(N + M)$ (to store the final union array, auxiliary space is $O(1)$).

#### 💻 Implementation (Python)
*Implement your solution directly in [union_arrays.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/union_arrays.py).*

---

### 10. Intersection of Two Sorted Arrays
*   **Video Link:** [Video Tutorial](https://www.youtube.com/watch?v=wvcQg43_V8M&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=12)
*   **Implementation:** [intersection_arrays.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/intersection_arrays.py)
*   **Difficulty:** Easy/Medium

#### 💡 Problem Statement
Given two sorted arrays `arr1` and `arr2`, find the intersection of these two arrays. The intersection array should contain common elements, matching duplicates if they are common to both, sorted in ascending order.

#### 📐 ASCII Visualization (Two Pointer Comparison)
Assume `arr1 = [ 1, 2, 2, 3, 4 ]` and `arr2 = [ 2, 2, 3, 5 ]`.
Set pointers `i = 0` (points to `arr1`), `j = 0` (points to `arr2`).

```text
Step 1: arr1[i] = 1, arr2[j] = 2. Since 1 < 2, increment i.
   arr1: [ 1, 2, 2, 3, 4 ]   arr2: [ 2, 2, 3, 5 ]
             ^                         ^
             i                         j

Step 2: arr1[i] = 2, arr2[j] = 2. They are equal! Add 2 to intersection. Increment both i and j.
intersection: [ 2 ]
   arr1: [ 1, 2, 2, 3, 4 ]   arr2: [ 2, 2, 3, 5 ]
                ^                         ^
                i                         j

Step 3: arr1[i] = 2, arr2[j] = 2. They are equal! Add 2 to intersection. Increment both.
intersection: [ 2, 2 ]
   arr1: [ 1, 2, 2, 3, 4 ]   arr2: [ 2, 2, 3, 5 ]
                   ^                         ^
                   i                         j

Step 4: arr1[i] = 3, arr2[j] = 3. They are equal! Add 3 to intersection. Increment both.
intersection: [ 2, 2, 3 ]
   arr1: [ 1, 2, 2, 3, 4 ]   arr2: [ 2, 2, 3, 5 ]
                      ^                         ^
                      i                         j

Step 5: arr1[i] = 4, arr2[j] = 5. Since 4 < 5, increment i.
   arr1: [ 1, 2, 2, 3, 4 ]   arr2: [ 2, 2, 3, 5 ]
                         ^                      ^
                        (end)                   j

Result: [ 2, 2, 3 ]
```

#### ⚙️ Approaches & Complexity

##### 1. Brute Force (Using Visited Array)
*   **Idea:** For each element in `arr1`, search it in `arr2`. To handle duplicate elements correctly, keep a boolean "visited" array of size `M` for `arr2` so that we do not match the same element twice.
*   **Time Complexity:** $O(N \times M)$
*   **Space Complexity:** $O(M)$ (visited array).

##### 2. Optimal Approach (Two Pointers)
*   **Idea:** Since both arrays are already sorted, use a two-pointer approach comparing the current elements of both arrays.
    - If `arr1[i] == arr2[j]`, append it to the result list, and increment both `i` and `j`.
    - If `arr1[i] < arr2[j]`, increment `i`.
    - If `arr1[i] > arr2[j]`, increment `j`.
*   **Time Complexity:** $O(N + M)$ (single pass through both arrays).
*   **Space Complexity:** $O(\min(N, M))$ (to store the final intersection array, auxiliary space is $O(1)$).

#### 💻 Implementation (Python)
*Implement your solution directly in [intersection_arrays.py](file:///Users/natesh/projects/system-design/dsa-coding-patterns/leetcode/arrays/intersection_arrays.py).*



