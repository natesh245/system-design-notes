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
    result = []

    i = 0
    j= 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if (not result or result[-1]!= arr1[i]) :
                result.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            if (not result or result[-1]!= arr2[j]) : 
                result.append(arr2[j])
            j+=1
        elif arr1[i] == arr2[j]:
            if (not result or result[-1]!=arr1[i]) :
                result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if (not result or result[-1]!=arr1[i]):
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if (not result or result[-1]!=arr2[j]):
            result.append(arr2[j])
        j += 1

      

    return result


    



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
        {"arr1": [], "arr2": [], "expected": [], "description": "Both arrays empty"},
        {"arr1": [-5, -3, -1], "arr2": [-4, -3, 0], "expected": [-5, -4, -3, -1, 0], "description": "Negative numbers"},
        {"arr1": [-10, -5, 0, 5], "arr2": [-5, 0, 10], "expected": [-10, -5, 0, 5, 10], "description": "Mixed negative, zero, and positive"},
        {"arr1": [5], "arr2": [], "expected": [5], "description": "Single element first array, second empty"},
        {"arr1": [], "arr2": [10], "expected": [10], "description": "First empty, single element second array"},
        {"arr1": [1, 3, 5, 7, 7, 9], "arr2": [2, 4, 6, 8, 8, 10], "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "description": "Interleaved elements with duplicates"},
        {"arr1": [1, 2, 3, 4, 5], "arr2": [2, 3, 4], "expected": [1, 2, 3, 4, 5], "description": "Second array is subset of first"},
        {"arr1": [2, 2, 2], "arr2": [2, 2], "expected": [2], "description": "All elements identical across both arrays"},
        {"arr1": [1, 1, 1, 5, 5], "arr2": [1, 2, 2, 5, 6], "expected": [1, 2, 5, 6], "description": "Multiple repeated frequency blocks"},
        {"arr1": [0, 0, 0], "arr2": [-1, 0, 1], "expected": [-1, 0, 1], "description": "Zero handling with duplicates"},
        {"arr1": [10**5, 10**7], "arr2": [10**4, 10**5], "expected": [10**4, 10**5, 10**7], "description": "Large numerical values"},
        {"arr1": [1]*50 + [2]*50, "arr2": [2]*50 + [3]*50, "expected": [1, 2, 3], "description": "Large repeated runs of single numbers"},
        {"arr1": list(range(0, 100, 2)), "arr2": list(range(1, 100, 2)), "expected": list(range(100)), "description": "Large even/odd interleaved arrays"},
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
