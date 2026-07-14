def find_largest_element(arr):
    """
    Problem: Find the largest element in an array.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param arr: List of numbers
    :return: The largest number in the list
    """
    # TODO: Implement this function
    largest = arr[0]

    for num in arr[1:]:
        if num>largest:
            largest = num
    return largest


    

# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [3, 2, 1, 5, 2], "expected": 5, "description": "Unsorted array with positive numbers"},
        {"arr": [8, 10, 5, 7, 9], "expected": 10, "description": "Unsorted array with max in middle"},
        {"arr": [-1, -5, -3, -2], "expected": -1, "description": "All negative numbers"},
        {"arr": [42], "expected": 42, "description": "Single element array"},
        {"arr": [7, 7, 7, 7], "expected": 7, "description": "All elements are equal"},
        {"arr": [1.5, 2.8, 0.9, 2.79], "expected": 2.8, "description": "Floating point numbers"},
        {"arr": [-10, 0, 10, 5], "expected": 10, "description": "Mixed positive and negative numbers"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        try:
            result = find_largest_element(test["arr"])
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
