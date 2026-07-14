def is_sorted(arr):
    """
    Problem: Check if the array is sorted in non-decreasing (ascending) order.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param arr: List of numbers
    :return: True if the array is sorted, False otherwise.
    """
    # TODO: Implement this function

    if not arr or len(arr)==1:
        return True

    for i in range(1,len(arr)):
        if arr[i] >= arr[i-1]:
            continue
            
        else:
            return False
    return True


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [1, 2, 3, 4, 5], "expected": True, "description": "Strictly increasing sorted array"},
        {"arr": [1, 2, 2, 4, 5], "expected": True, "description": "Sorted array with duplicates"},
        {"arr": [5, 4, 3, 2, 1], "expected": False, "description": "Strictly decreasing array"},
        {"arr": [1, 3, 2, 4, 5], "expected": False, "description": "Unsorted array"},
        {"arr": [42], "expected": True, "description": "Single element array"},
        {"arr": [], "expected": True, "description": "Empty array"},
        {"arr": [-5, -3, -3, 0, 2], "expected": True, "description": "Sorted negative numbers"},
        {"arr": [1.1, 1.2, 1.2, 2.0], "expected": True, "description": "Sorted floating point numbers"},
        {"arr": [1.1, 1.0, 1.2], "expected": False, "description": "Unsorted floating point numbers"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        try:
            result = is_sorted(test["arr"])
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
