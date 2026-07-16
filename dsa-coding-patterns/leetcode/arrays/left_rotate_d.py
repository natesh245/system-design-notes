def left_rotate_d(arr, d):
    """
    Problem: Left rotate the array by d places in-place.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param arr: List of numbers
    :param d: Number of positions to rotate
    :return: The same list 'arr' modified in-place.
    """
    # TODO: Implement this function
    pass


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [1, 2, 3, 4, 5, 6, 7], "d": 3, "expected": [4, 5, 6, 7, 1, 2, 3], "description": "Rotate 3 places (d < N)"},
        {"arr": [1, 2, 3], "d": 3, "expected": [1, 2, 3], "description": "Rotate size of array (d == N)"},
        {"arr": [1, 2, 3], "d": 4, "expected": [2, 3, 1], "description": "Rotate more than size of array (d > N)"},
        {"arr": [1, 2, 3], "d": 0, "expected": [1, 2, 3], "description": "Rotate 0 places"},
        {"arr": [], "d": 5, "expected": [], "description": "Empty array"},
        {"arr": [5], "d": 10, "expected": [5], "description": "Single element array with large d"},
        {"arr": [1, 2], "d": 1, "expected": [2, 1], "description": "Array of size 2"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        arr_input = list(test["arr"])
        d_val = test["d"]
        try:
            left_rotate_d(arr_input, d_val)
            if arr_input == test["expected"]:
                print(f"✓ Test Case {i} ({test['description']}): Passed")
                passed_count += 1
            else:
                print(f"✗ Test Case {i} ({test['description']}): Failed. Expected {test['expected']}, got {arr_input}")
        except Exception as e:
            print(f"✗ Test Case {i} ({test['description']}): Failed with error: {str(e)}")

    print(f"\nTest Summary: {passed_count}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()
