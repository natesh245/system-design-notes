def move_zeros(arr):
    """
    Problem: Move all zeros to the end of the array in-place, 
    maintaining the relative order of non-zero elements.
    
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
        {"arr": [1, 0, 2, 3, 0, 4], "expected": [1, 2, 3, 4, 0, 0], "description": "Standard case with mixed zeros"},
        {"arr": [0, 1, 0, 3, 12], "expected": [1, 3, 12, 0, 0], "description": "Leecode example case"},
        {"arr": [1, 2, 3, 4], "expected": [1, 2, 3, 4], "description": "No zeros"},
        {"arr": [0, 0, 0], "expected": [0, 0, 0], "description": "All zeros"},
        {"arr": [2, 1, 0, 0], "expected": [2, 1, 0, 0], "description": "Zeros already at the end"},
        {"arr": [0], "expected": [0], "description": "Single element zero"},
        {"arr": [], "expected": [], "description": "Empty array"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        arr_input = list(test["arr"])
        try:
            move_zeros(arr_input)
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
