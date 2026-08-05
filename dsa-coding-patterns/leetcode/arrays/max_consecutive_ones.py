def max_consecutive_ones(nums):
    """
    Problem: Given a binary array nums, return the maximum number of consecutive 1's in the array.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param nums: List[int] containing binary elements (0 or 1)
    :return: int - maximum number of consecutive 1's
    """
    # TODO: Implement your solution here
    count = 0 
    maxCount = 0 

    for num in nums:
        if num == 1:
            count+=1
        else:
            
            count = 0
        maxCount = max(maxCount,count)
    return maxCount


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"nums": [1, 1, 0, 1, 1, 1], "expected": 3, "description": "Basic case with multiple runs of ones"},
        {"nums": [1, 0, 1, 1, 0, 1], "expected": 2, "description": "Multiple small runs of ones"},
        {"nums": [1, 1, 1, 1, 1], "expected": 5, "description": "All elements are ones"},
        {"nums": [0, 0, 0, 0], "expected": 0, "description": "All elements are zeros"},
        {"nums": [1], "expected": 1, "description": "Single element array with 1"},
        {"nums": [0], "expected": 0, "description": "Single element array with 0"},
        {"nums": [], "expected": 0, "description": "Empty array"},
        {"nums": [1, 0, 1, 0, 1, 0, 1], "expected": 1, "description": "Alternating ones and zeros"},
        {"nums": [1, 1, 1, 0, 0, 0], "expected": 3, "description": "Ones at the beginning"},
        {"nums": [0, 0, 0, 1, 1, 1, 1], "expected": 4, "description": "Ones at the end"},
        {"nums": [0, 0, 1, 0, 0], "expected": 1, "description": "Single one surrounded by zeros"},
        {"nums": [1, 1, 1, 1, 0, 1, 1], "expected": 4, "description": "Max run at start, smaller run later"},
        {"nums": [1, 1, 0, 1, 1, 1, 1, 1], "expected": 5, "description": "Max run at end, smaller run earlier"},
        {"nums": [0, 1, 1, 1, 0, 1, 1, 0], "expected": 3, "description": "Max run in the middle"},
        {"nums": [0, 1, 1], "expected": 2, "description": "Trailing ones after zero"},
        {"nums": [1, 1, 0], "expected": 2, "description": "Leading ones before zero"},
        {"nums": [1] * 100, "expected": 100, "description": "Large array with 100 ones"},
        {"nums": [0] * 100, "expected": 0, "description": "Large array with 100 zeros"},
        {"nums": [1] * 10 + [0] * 5 + [1] * 25 + [0] * 2 + [1] * 15, "expected": 25, "description": "Large array with mixed long runs"},
        {"nums": [0] * 99 + [1], "expected": 1, "description": "Large array with single 1 at the end"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        nums_input = list(test["nums"])
        try:
            result = max_consecutive_ones(nums_input)
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
