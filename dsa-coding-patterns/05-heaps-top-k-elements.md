# Chapter 5: Heaps & Top K Elements

Heaps (or Priority Queues) are binary tree structures optimized to fetch the minimum or maximum element in constant time $O(1)$. This chapter covers using heaps to find **Top K Elements** in $O(N \log K)$ time and implementing the **Two Heaps** pattern to calculate the running median of a dynamic data stream.

---

## 🏗️ 1. Lightweight JavaScript Min-Heap Implementation

Since JavaScript lacks a native heap class, you should be prepared to sketch a basic heap during coding interviews:

```javascript
class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() { return this.heap.length; }
    peek() { return this.heap[0]; }

    insert(val) {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }

    pop() {
        if (this.size() === 0) return null;
        const root = this.heap[0];
        const last = this.heap.pop();
        if (this.size() > 0) {
            this.heap[0] = last;
            this.bubbleDown(0);
        }
        return root;
    }

    bubbleUp(idx) {
        while (idx > 0) {
            const parentIdx = Math.floor((idx - 1) / 2);
            if (this.heap[idx] >= this.heap[parentIdx]) break;
            [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
            idx = parentIdx;
        }
    }

    bubbleDown(idx) {
        const length = this.heap.length;
        while (2 * idx + 1 < length) {
            let leftChildIdx = 2 * idx + 1;
            let rightChildIdx = 2 * idx + 2;
            let smallestIdx = leftChildIdx;

            if (rightChildIdx < length && this.heap[rightChildIdx] < this.heap[leftChildIdx]) {
                smallestIdx = rightChildIdx;
            }

            if (this.heap[idx] <= this.heap[smallestIdx]) break;
            [this.heap[idx], this.heap[smallestIdx]] = [this.heap[smallestIdx], this.heap[idx]];
            idx = smallestIdx;
        }
    }
}
```

---

## 🔝 2. The Top K Elements Pattern

### Concept:
To find the top $K$ largest items in an unsorted array of size $N$:
1.  Initialize a **Min-Heap** of size $K$.
2.  Add the first $K$ elements to the heap.
3.  For each remaining element $X$ in the array:
    *   Compare $X$ with the root (minimum) of the heap.
    *   If $X > \text{root}$, pop the root and insert $X$ into the heap.
4.  After scanning the array, the heap will contain the $K$ largest elements.

*   **Complexity:**
    *   Time Complexity: $O(N \log K)$ — Insertion in heap of size $K$ takes $O(\log K)$ time, performed for $N$ elements. (Much faster than sorting the entire array, which takes $O(N \log N)$).
    *   Space Complexity: $O(K)$ — Space required to store $K$ elements.

### 📚 Code Solution: Kth Largest Element in an Array
```javascript
function findKthLargest(nums, k) {
    const minHeap = new MinHeap();

    // 1. Fill heap to size K
    for (let i = 0; i < k; i++) {
        minHeap.insert(nums[i]);
    }

    // 2. Iterate remaining elements
    for (let i = k; i < nums.length; i++) {
        if (nums[i] > minHeap.peek()) {
            minHeap.pop(); // Remove smallest
            minHeap.insert(nums[i]); // Add larger
        }
    }

    return minHeap.peek(); // Root is the Kth largest element
}
```

---

## 🤹 3. The Two Heaps Pattern (Running Median)

### Concept:
To find the median of a stream of numbers:
*   We divide numbers into two halves: a lower half and an upper half.
*   **Max-Heap (`maxHeap`):** Stores the lower half of numbers (the root returns the maximum of the lower half).
*   **Min-Heap (`minHeap`):** Stores the upper half of numbers (the root returns the minimum of the upper half).
*   **Balance Constraint:** The size difference between both heaps must be $\le 1$.

```text
                  +--------------------------------+
                  |         Incoming Stream        |
                  +---------------+----------------+
                                  |
            [ Split elements into lower & upper halves ]
                                  |
         +------------------------+------------------------+
         |                                                 |
+--------v--------+                               +--------v--------+
| Max-Heap (Lower)|                               | Min-Heap (Upper)|
|  eg: [ 3, 1 ]   |                               |  eg: [ 5, 4 ]   |
|   peek() = 3    |                               |   peek() = 4    |
+--------+--------+                               +--------+--------+
         |                                                 |
         +------------------------+------------------------+
                                  |
              Median = (maxHeap.peek() + minHeap.peek()) / 2
                     = (3 + 4) / 2 = 3.5
```

---

### 📚 Code Solution: Median of a Data Stream
```javascript
// Note: Assume MaxHeap is implemented similarly to MinHeap 
// but using a greater-than check during heapify swaps.

class MedianFinder {
    constructor() {
        this.maxHeap = new MaxHeap(); // Lower half
        this.minHeap = new MinHeap(); // Upper half
    }

    addNum(num) {
        // 1. Insert number
        if (this.maxHeap.size() === 0 || num <= this.maxHeap.peek()) {
            this.maxHeap.insert(num);
        } else {
            this.minHeap.insert(num);
        }

        // 2. Rebalance Heaps
        if (this.maxHeap.size() > this.minHeap.size() + 1) {
            this.minHeap.insert(this.maxHeap.pop());
        } else if (this.minHeap.size() > this.maxHeap.size()) {
            this.maxHeap.insert(this.minHeap.pop());
        }
    }

    findMedian() {
        if (this.maxHeap.size() === this.minHeap.size()) {
            // Even number of elements: average of roots
            return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
        } else {
            // Odd number: root of maxHeap (lower half holds the extra element)
            return this.maxHeap.peek();
        }
    }
}
```
*   **Complexity:**
    *   Time Complexity: `addNum` runs in $O(\log N)$ time; `findMedian` runs in $O(1)$ time.
    *   Space Complexity: $O(N)$ — Storing all numbers across two heaps.
