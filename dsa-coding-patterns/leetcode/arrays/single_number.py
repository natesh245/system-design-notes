

from collections import defaultdict
def single_number(nums):
    """
    Problem: Given a non-empty array of integers nums, every element appears twice except for one element 
    which appears exactly once. Find that single element.
    
    Time Complexity Goal: O(N)
    Space Complexity Goal: O(1)
    
    :param nums: List[int] non-empty array where every element except one appears twice
    :return: int - the single element
    """
    # TODO: Implement your solution here
    counter = defaultdict(int)


    for num in nums:
        counter[num]+=1
    
    
    
    for key in counter:
        if counter[key] == 1:
            return key


   


    


# --- Test Cases ---
def run_tests():
    test_cases = [
        {"nums": [2, 2, 1], "expected": 1, "description": "Basic case with single element at the end"},
        {"nums": [4, 1, 2, 1, 2], "expected": 4, "description": "Single element at the beginning"},
        {"nums": [1], "expected": 1, "description": "Single element array"},
        {"nums": [-1, -1, -2], "expected": -2, "description": "Negative numbers with single element at end"},
        {"nums": [2, 2, -3, 5, 5], "expected": -3, "description": "Single negative number with positive pairs"},
        {"nums": [1, 0, 1], "expected": 0, "description": "Single element is zero"},
        {"nums": [5, 5, 0], "expected": 0, "description": "Single element is zero at end"},
        {"nums": [7, 7, 8, 8, 9], "expected": 9, "description": "Pairs followed by single element"},
        {"nums": [9, 7, 7, 8, 8], "expected": 9, "description": "Single element followed by pairs"},
        {"nums": [100000, 200000, 100000], "expected": 200000, "description": "Large integer values"},
        {"nums": [10, 20, 30, 20, 10], "expected": 30, "description": "Single element in the middle of pairs"},
        {"nums": [-100, 200, -100], "expected": 200, "description": "Negative duplicate pair with positive single"},
        {"nums": [i for i in range(1, 51) for _ in range(2)] + [999], "expected": 999, "description": "Large array with 50 pairs and single element at end"},
        {"nums": [0, 0, 5], "expected": 5, "description": "Pair of zeros and single positive integer"},
        {"nums": [-5, -10, -5], "expected": -10, "description": "Negative numbers pair with single negative integer"},
        {"nums": [1, 2, 3, 2, 1], "expected": 3, "description": "Palindromic pair structure with single element at center"},
        {"nums": [42, 1, 2, 3, 4, 4, 3, 2, 1, 42, 99, 100, 100, 99, 7], "expected": 7, "description": "Multiple nested pairs with single element at end"},
        {"nums": [-1], "expected": -1, "description": "Single element array with -1"},
        {"nums": [0], "expected": 0, "description": "Single element array with 0"},
        {"nums": [12345, 67890, 12345], "expected": 67890, "description": "Scattered distinct large numbers"},
    ]

    passed_count = 0

    for i, test in enumerate(test_cases, 1):
        nums_input = list(test["nums"])
        try:
            result = single_number(nums_input)
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
