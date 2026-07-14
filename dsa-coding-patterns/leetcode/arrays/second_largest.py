def find_second_largest(arr):
    """
    Problem: Find the second largest element in an array without sorting.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param arr: List of numbers
    :return: The second largest number in the list, or -1 if it does not exist.
    """
    # TODO: Implement this function

    if not arr:
        return -1
    largest = -float('inf')
    second_largest = -float('inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num <largest:
            second_largest = num 
        

    return second_largest if second_largest != -float('inf') else -1


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [12, 35, 1, 10, 34, 1], "expected": 34, "description": "Standard unsorted array"},
        {"arr": [10, 5, 10], "expected": 5, "description": "Array with duplicate largest elements"},
        {"arr": [10, 10, 10], "expected": -1, "description": "All elements are equal"},
        {"arr": [-1, -2, -3, -4], "expected": -2, "description": "All negative numbers"},
        {"arr": [42], "expected": -1, "description": "Single element array"},
        {"arr": [], "expected": -1, "description": "Empty array"},
        {"arr": [1.5, 2.8, 0.9, 2.79], "expected": 2.79, "description": "Floating point numbers"},
        {"arr": [2, 1], "expected": 1, "description": "Two elements, descending"},
        {"arr": [1, 2], "expected": 1, "description": "Two elements, ascending"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        try:
            result = find_second_largest(test["arr"])
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
