
def intersection_arrays(arr1, arr2):
    """
    Problem: Find the intersection of two sorted arrays. The returned array 
    should contain common elements, matching duplicates if they are common to both,
    and must be sorted in ascending order.
    
    Time Complexity Goal: O(N + M)
    Space Complexity Goal: O(min(N, M)) (to store the result)
    
    :param arr1: List of sorted numbers
    :param arr2: List of sorted numbers
    :return: Sorted list containing the intersection of elements.
    """

    if not arr1 or not arr2:
        return []
   
    result = [ ]
    p1 = 0
    p2 = 0

    while p1 < len(arr1) and p2<len(arr2): 

        if arr1[p1]==arr2[p2]:
            result.append(arr1[p1])
            p1+=1
            p2+=1
        elif arr1[p1]<arr2[p2]:
            p1+=1
        else:
            p2+=1

    return result


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr1": [1, 2, 2, 3, 4], "arr2": [2, 2, 3, 5], "expected": [2, 2, 3], "description": "Overlapping arrays with duplicate matches"},
        {"arr1": [1, 2, 3], "arr2": [4, 5, 6], "expected": [], "description": "Disjoint arrays"},
        {"arr1": [], "arr2": [1, 2], "expected": [], "description": "First array empty"},
        {"arr1": [1, 2], "arr2": [], "expected": [], "description": "Second array empty"},
        {"arr1": [], "arr2": [], "expected": [], "description": "Both arrays empty"},
        {"arr1": [1, 1, 1], "arr2": [1, 1], "expected": [1, 1], "description": "Arrays with unequal duplicate occurrences"},
        {"arr1": [2, 3, 4], "arr2": [2, 3, 4], "expected": [2, 3, 4], "description": "Identical arrays"},
        {"arr1": [3, 4, 5], "arr2": [1, 3, 5], "expected": [3, 5], "description": "Partially overlapping disjoint values"},
        {"arr1": [-10, -5, 0, 5, 10], "arr2": [-5, 0, 7, 10], "expected": [-5, 0, 10], "description": "Negative numbers and zero"},
        {"arr1": [1, 2, 3], "arr2": [3, 4, 5], "expected": [3], "description": "Boundary element intersection"},
        {"arr1": [9], "arr2": [9], "expected": [9], "description": "Single element identical"},
        {"arr1": [1], "arr2": [2], "expected": [], "description": "Single element distinct"},
        {"arr1": [1, 1, 2, 2, 3, 3], "arr2": [1, 2, 2, 3], "expected": [1, 2, 2, 3], "description": "Multiple duplicate clusters"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        arr1_input = list(test["arr1"])
        arr2_input = list(test["arr2"])
        try:
            result = intersection_arrays(arr1_input, arr2_input)
            if result == test["expected"]:
                print(f"✓ Test Case {i} ({test['description']}): Passed")
                passed_count += 1
            else:
                print(f"✗ Test Case {i} ({test['description']}): Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"✗ Test Case {i} ({test['description']}): Failed with error: {str(e)}")

    print(f"\nTest Summary: {passed_count}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()
