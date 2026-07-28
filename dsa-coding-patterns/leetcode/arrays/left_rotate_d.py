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
    arr_len = len(arr)
    if not arr:
        return arr
    
    if arr_len <= d:
        d = d % arr_len
    
    if d==0:
        return arr
    
    temp = arr[:d]

    for i  in range(d,len(arr)):
        arr[i-d]=arr[i]

    for j in range(d):
        arr[arr_len - d + j] = temp[j]

    return arr




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
        {"arr": [-1, -2, -3, -4], "d": 2, "expected": [-3, -4, -1, -2], "description": "Array with negative numbers"},
        {"arr": [7, 7, 7, 7], "d": 3, "expected": [7, 7, 7, 7], "description": "Array with all identical elements"},
        {"arr": [1, 2, 3, 4], "d": 100, "expected": [1, 2, 3, 4], "description": "d is an exact multiple of N (d % N == 0)"},
        {"arr": [10, 20, 30, 40, 50], "d": 12, "expected": [30, 40, 50, 10, 20], "description": "Large d (12 % 5 == 2)"},
        {"arr": [1, 2, 1, 2], "d": 1, "expected": [2, 1, 2, 1], "description": "Array with duplicates"},
        {"arr": [100, 200], "d": 3, "expected": [200, 100], "description": "Array of size 2 with d=3"},
        {"arr": list(range(100)), "d": 25, "expected": list(range(25, 100)) + list(range(25)), "description": "Large array of size 100 rotated by 25"},
        {"arr": [0, -5, 0, 5], "d": 3, "expected": [5, 0, -5, 0], "description": "Mixed zeros and negative numbers"},
        {"arr": [1, 2, 3, 4, 5], "d": 4, "expected": [5, 1, 2, 3, 4], "description": "Rotate by N-1 places"},
        {"arr": [42], "d": 0, "expected": [42], "description": "Single element with d=0"},
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
