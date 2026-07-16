def union_arrays(arr1, arr2):
    """
    Problem: Find the union of two sorted arrays. The returned union array 
    should contain only unique elements and must be sorted in ascending order.
    
    Time Complexity Goal: O(N + M)
    Space Complexity Goal: O(N + M) (to store the result)
    
    :param arr1: List of sorted numbers
    :param arr2: List of sorted numbers
    :return: Sorted list containing the union of unique elements.
    """
    # TODO: Implement this function
    pass


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr1": [1, 2, 3, 4, 5], "arr2": [2, 3, 5, 6], "expected": [1, 2, 3, 4, 5, 6], "description": "Overlapping arrays"},
        {"arr1": [1, 1, 2, 2], "arr2": [2, 3, 3], "expected": [1, 2, 3], "description": "Arrays with internal duplicates"},
        {"arr1": [], "arr2": [1, 2], "expected": [1, 2], "description": "First array empty"},
        {"arr1": [1, 2], "arr2": [], "expected": [1, 2], "description": "Second array empty"},
        {"arr1": [1, 2, 3], "arr2": [4, 5, 6], "expected": [1, 2, 3, 4, 5, 6], "description": "Non-overlapping disjoint arrays"},
        {"arr1": [3, 4, 5], "arr2": [1, 2], "expected": [1, 2, 3, 4, 5], "description": "Second array smaller elements disjoint"},
        {"arr1": [1], "arr2": [1], "expected": [1], "description": "Single element identical arrays"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        arr1_input = list(test["arr1"])
        arr2_input = list(test["arr2"])
        try:
            result = union_arrays(arr1_input, arr2_input)
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
