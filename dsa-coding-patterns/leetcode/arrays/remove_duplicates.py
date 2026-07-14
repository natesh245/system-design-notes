def remove_duplicates(arr):
    """
    Problem: Remove duplicates in-place from a sorted array and return the number of unique elements.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param arr: List of numbers (sorted in non-decreasing order)
    :return: The number of unique elements (k). The first k elements of arr should be updated to contain these unique elements.
    """
    # TODO: Implement this function
    if not arr:
        return 0

    i = 0

    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i=i+1
            arr[i] = arr[j]
    return i+1


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [1, 1, 2], "expected_k": 2, "expected_arr": [1, 2], "description": "Simple duplicates at start"},
        {"arr": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], "expected_k": 5, "expected_arr": [0, 1, 2, 3, 4], "description": "Multiple duplicates"},
        {"arr": [1, 2, 3, 4, 5], "expected_k": 5, "expected_arr": [1, 2, 3, 4, 5], "description": "Already unique sorted array"},
        {"arr": [1, 1, 1, 1], "expected_k": 1, "expected_arr": [1], "description": "All elements are equal"},
        {"arr": [42], "expected_k": 1, "expected_arr": [42], "description": "Single element array"},
        {"arr": [], "expected_k": 0, "expected_arr": [], "description": "Empty array"},
        {"arr": [-5, -5, -3, 0, 0, 2], "expected_k": 4, "expected_arr": [-5, -3, 0, 2], "description": "Sorted negative numbers and duplicates"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        try:
            arr_copy = list(test["arr"])  # Copy to modify in-place
            k = remove_duplicates(arr_copy)
            
            # Check length and contents of unique subsegment
            if k == test["expected_k"] and arr_copy[:k] == test["expected_arr"]:
                print(f"✓ Test Case {i} ({test['description']}): Passed")
                passed_count += 1
            else:
                print(f"✗ Test Case {i} ({test['description']}): Failed. Expected k={test['expected_k']}, unique_arr={test['expected_arr']}. Got k={k}, unique_arr={arr_copy[:k]}")
        except Exception as e:
            print(f"✗ Test Case {i} ({test['description']}): Failed with error: {str(e)}")

    print(f"\nTest Summary: {passed_count}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()
