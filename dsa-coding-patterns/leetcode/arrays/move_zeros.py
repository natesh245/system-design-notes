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
    if not arr or len(arr)==1:
        return arr
    i =  arr.index(0) if 0 in arr else -1

    if i==-1:
        return arr
    
    j=i+1

    while j<len(arr):
        if arr[j]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            if arr[i+1]==0:
                i+=1
            else:
                i=j
        

       
        j+=1

    return arr


   



    


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"arr": [1, 0, 2, 3, 0, 4], "expected": [1, 2, 3, 4, 0, 0], "description": "Standard case with mixed zeros"},
        {"arr": [0, 1, 0, 3, 12], "expected": [1, 3, 12, 0, 0], "description": "LeetCode example case"},
        {"arr": [1, 2, 3, 4], "expected": [1, 2, 3, 4], "description": "No zeros"},
        {"arr": [0, 0, 0], "expected": [0, 0, 0], "description": "All zeros"},
        {"arr": [2, 1, 0, 0], "expected": [2, 1, 0, 0], "description": "Zeros already at the end"},
        {"arr": [0], "expected": [0], "description": "Single element zero"},
        {"arr": [], "expected": [], "description": "Empty array"},
        {"arr": [0, 0, 1], "expected": [1, 0, 0], "description": "Multiple consecutive zeros at start"},
        {"arr": [0, 1, 0, 2, 0, 3], "expected": [1, 2, 3, 0, 0, 0], "description": "Alternating zeros and non-zeros"},
        {"arr": [-1, 0, -3, 0, 5], "expected": [-1, -3, 5, 0, 0], "description": "Negative numbers with zeros"},
        {"arr": [0, 0, 0, 1, 2], "expected": [1, 2, 0, 0, 0], "description": "Multiple zeros before non-zeros"},
        {"arr": [1, 2, 3, 0], "expected": [1, 2, 3, 0], "description": "Single zero at the end"},
        {"arr": [1, 0, 0, 0, 0, 0, 2], "expected": [1, 2, 0, 0, 0, 0, 0], "description": "Many consecutive zeros between non-zeros"},
        {"arr": [5], "expected": [5], "description": "Single non-zero element"},
        {"arr": [0, 5, 0, 10, 0, 15, 0, 20], "expected": [5, 10, 15, 20, 0, 0, 0, 0], "description": "Interleaved zeros and multiples of 5"},
        {"arr": [0, 0, 0, 0, 1], "expected": [1, 0, 0, 0, 0], "description": "4 zeros followed by 1"},
        {"arr": [-5, -4, -3, 0, -2, -1], "expected": [-5, -4, -3, -2, -1, 0], "description": "Negative integers with single zero in middle"},
        {"arr": [100, 0, 200, 0, 300], "expected": [100, 200, 300, 0, 0], "description": "Large values with interleaved zeros"},
        {"arr": list(range(1, 10)) + [0]*10, "expected": list(range(1, 10)) + [0]*10, "description": "Sequential numbers followed by 10 zeros"},
        {"arr": [0]*5 + list(range(1, 10)), "expected": list(range(1, 10)) + [0]*5, "description": "5 zeros followed by sequential numbers"},
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
