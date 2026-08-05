def missing_number(nums):
    """
    Problem: Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param nums: List[int] containing n distinct integers in range [0, n]
    :return: int - the missing number
    """
    # TODO: Implement your solution here
    pass


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"nums": [3, 0, 1], "expected": 2, "description": "Small basic unsorted array"},
        {"nums": [0, 1], "expected": 2, "description": "Small consecutive missing end"},
        {"nums": [1, 2], "expected": 0, "description": "Small consecutive missing start (0)"},
        {"nums": [0], "expected": 1, "description": "Single element array 0"},
        {"nums": [1], "expected": 0, "description": "Single element array 1"},
        {"nums": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8, "description": "Larger array missing middle element"},
        {"nums": [0, 1, 2, 3, 4], "expected": 5, "description": "Sorted array missing last element n"},
        {"nums": [1, 2, 3, 4, 5], "expected": 0, "description": "Sorted array missing first element 0"},
        {"nums": [5, 4, 2, 1, 0], "expected": 3, "description": "Reverse sorted array missing middle element"},
        {"nums": [2, 0, 3, 1], "expected": 4, "description": "Unsorted array missing last element"},
        {"nums": [0, 1, 2, 3, 4, 6, 7, 8, 9, 10], "expected": 5, "description": "N=10 missing middle element 5"},
        {"nums": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "expected": 0, "description": "N=10 missing 0"},
        {"nums": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "expected": 10, "description": "N=10 missing 10"},
        {"nums": [6, 3, 0, 5, 2, 1, 7], "expected": 4, "description": "N=7 unsorted missing 4"},
        {"nums": [0, 2], "expected": 1, "description": "Two elements missing 1"},
        {"nums": [1, 2], "expected": 0, "description": "Two elements missing 0"},
        {"nums": [0, 1], "expected": 2, "description": "Two elements missing 2"},
        {"nums": list(range(500)) + list(range(501, 1001)), "expected": 500, "description": "Large array N=1000 missing 500"},
        {"nums": list(range(1, 1001)), "expected": 0, "description": "Large array N=1000 missing 0"},
        {"nums": list(range(1000)), "expected": 1000, "description": "Large array N=1000 missing 1000"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        nums_input = list(test["nums"])
        try:
            result = missing_number(nums_input)
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
