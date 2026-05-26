# Chapter 2: Fast & Slow Pointers & Merge Intervals

This chapter covers two critical patterns used for path evaluation in cyclic data structures (Linked Lists) and coordination of time intervals (scheduling/calendaring).

---

## 🐢🐇 1. The Fast & Slow Pointers Pattern

### Concept:
Also known as **Floyd's Cycle-Finding Algorithm** (or the Tortoise and Hare algorithm), this approach uses two pointers moving at different speeds through a Linked List or Array. The **slow** pointer moves one step at a time, while the **fast** pointer moves two steps. If a cycle exists, the fast pointer will loop around and meet the slow pointer.

### 📐 ASCII Visualization (Cycle Detection)
```text
Linked List: 1 -> 2 -> 3 -> 4 -> 5
                       ^         |
                       |         v
                       +--------- 6  (Cycle: 6 points to 3)

Step 1: Init pointers at head (1)
[1] -> 2 -> 3 -> 4 -> 5 -> 6 -> (3)
S, F

Step 2: S moves 1 step, F moves 2 steps
1 -> [2] -> 3 -> [4] -> 5 -> 6 -> (3)
      S           F

Step 3: S moves 1 step, F moves 2 steps
1 -> 2 -> [3] -> 4 -> 5 -> [6] -> (3)
           S                F

Step 4: S moves 1 step, F moves 2 steps (F wraps around cycle)
1 -> 2 -> 3 -> [4] -> [5] -> 6 -> (3)
                S, F   (S and F meet! Cycle Detected!)
```

---

### 💻 Code Template (Cycle Detection in Linked List)
```javascript
function hasCycle(head) {
    if (!head || !head.next) return false;

    let slow = head;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;         // 1 step
        fast = fast.next.next;    // 2 steps

        if (slow === fast) {
            return true; // Fast pointer caught up to slow (cycle exists)
        }
    }
    return false;
}
```

---

### 📚 Core Problems & Solutions

#### Problem 1: Middle of the Linked List
*   **Problem:** Find the middle node of a Linked List. If there are two middle nodes, return the second middle node.
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Single pass where fast pointer reaches end in $N/2$ steps.
    *   Space Complexity: $O(1)$ — Two pointers.
*   **Implementation:**
    ```javascript
    function middleNode(head) {
        let slow = head;
        let fast = head;

        while (fast !== null && fast.next !== null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow; // When fast reaches end, slow is exactly in the middle
    }
    ```

#### Problem 2: Happy Number cycle detection
*   **Problem:** Determine if a number $n$ is "happy". A happy number is defined by a process where we replace the number with the sum of the squares of its digits repeatedly, until it equals 1. If it loops endlessly in a cycle, it is not happy.
*   **Complexity:**
    *   Time Complexity: $O(\log N)$ — The number of digits decreases logarithmically.
    *   Space Complexity: $O(1)$ — No hash set is used; cycle is detected using Tortoise & Hare.
*   **Implementation:**
    ```javascript
    function getNext(number) {
        let totalSum = 0;
        while (number > 0) {
            const d = number % 10;
            totalSum += d * d;
            number = Math.floor(number / 10);
        }
        return totalSum;
    }

    function isHappy(n) {
        let slow = n;
        let fast = getNext(n);

        while (fast !== 1 && slow !== fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }

        return fast === 1;
    }
    ```

---

## 🗓️ 2. The Merge Intervals Pattern

### Concept:
The Merge Intervals pattern is used to handle overlapping intervals. The core mechanism is:
1.  **Sort** the intervals by their start times.
2.  Compare the start time of the current interval with the end time of the previous interval to detect overlap.
3.  If they overlap, merge them by updating the previous interval's end time.

### 📐 ASCII Visualization (Merging Overlaps)
```text
Interval A: [1, 4]
Interval B: [2, 5]
Interval C: [7, 9]

Sorted Input:
[1, 4] ------
  [2, 5] ------
           [7, 9] ------

Step 1: Check A and B. Since B.start (2) <= A.end (4), they overlap!
Merge: New End = Max(A.end, B.end) = Max(4, 5) = 5.
Merged List: [[1, 5]]

Step 2: Check C. Since C.start (7) > Merged.end (5), no overlap.
Add C to list.
Merged List: [[1, 5], [7, 9]]
```

---

### 💻 Code Template (Interval Merging)
```javascript
function mergeIntervals(intervals) {
    if (intervals.length <= 1) return intervals;

    // 1. Sort by start times
    intervals.sort((a, b) => a[0] - b[0]);

    const merged = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const current = intervals[i];
        const lastMerged = merged[merged.length - 1];

        // 2. Check for overlap: current start <= lastMerged end
        if (current[0] <= lastMerged[1]) {
            // Overlap: Merge by expanding the end boundary
            lastMerged[1] = Math.max(lastMerged[1], current[1]);
        } else {
            // No overlap: Add current interval directly
            merged.push(current);
        }
    }

    return merged;
}
```

---

### 📚 Core Problems & Solutions

#### Problem 1: Insert Interval
*   **Problem:** Given a set of non-overlapping intervals sorted by start time, insert a `newInterval` into the set (merging if necessary).
*   **Complexity:**
    *   Time Complexity: $O(N)$ — Single pass scan.
    *   Space Complexity: $O(N)$ — Output array.
*   **Implementation:**
    ```javascript
    function insert(intervals, newInterval) {
        const result = [];
        let i = 0;
        const n = intervals.length;

        // 1. Add all intervals that end before the new interval starts
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push(intervals[i]);
            i++;
        }

        // 2. Merge all overlapping intervals with newInterval
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push(newInterval); // Push final merged interval

        // 3. Add remaining intervals
        while (i < n) {
            result.push(intervals[i]);
            i++;
        }

        return result;
    }
    ```
