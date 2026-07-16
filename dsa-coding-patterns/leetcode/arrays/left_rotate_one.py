def left_rotate_one(arr):
    """
    Problem: Left rotate the array by one place in-place.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param arr: List of numbers
    :return: The same list 'arr' modified in-place.
    """
    # TODO: Implement this function
    pass


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [1, 2, 3, 4, 5], "expected": [2, 3, 4, 5, 1], "description": "Standard array of size 5"},
        {"arr": [1, 2], "expected": [2, 1], "description": "Array of size 2"},
        {"arr": [3], "expected": [3], "description": "Single element array"},
        {"arr": [], "expected": [], "description": "Empty array"},
        {"arr": [5, 5, 5], "expected": [5, 5, 5], "description": "Array with identical elements"},
        {"arr": [-1, -2, -3], "expected": [-2, -3, -1], "description": "Array with negative numbers"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        # Make a copy of the original array to print in case of failure, and to pass to the function
        arr_input = list(test["arr"])
        try:
            left_rotate_one(arr_input)
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
