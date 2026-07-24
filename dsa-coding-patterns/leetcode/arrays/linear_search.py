def linear_search(arr, num):
    """
    Problem: Find the index of the first occurrence of 'num' in the array 'arr'.
    If 'num' is not present in the array, return -1.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param arr: List of numbers
    :param num: Target number to find
    :return: Index of 'num' if found, else -1.
    """
    # TODO: Implement this function
    for i,n in enumerate(arr):
        if n == num:
            return i
    return -1
    


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [1, 2, 3, 4, 5], "num": 3, "expected": 2, "description": "Element present in middle"},
        {"arr": [5, 4, 3, 2, 1], "num": 6, "expected": -1, "description": "Element not present"},
        {"arr": [3, 3, 3], "num": 3, "expected": 0, "description": "Multiple occurrences (return first index)"},
        {"arr": [], "num": 5, "expected": -1, "description": "Empty array"},
        {"arr": [-5, -3, 0, 2], "num": -3, "expected": 1, "description": "Negative target element"},
        {"arr": [42], "num": 42, "expected": 0, "description": "Single element present"},
        {"arr": [42], "num": 100, "expected": -1, "description": "Single element not present"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        arr_input = list(test["arr"])
        num_val = test["num"]
        try:
            result = linear_search(arr_input, num_val)
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
