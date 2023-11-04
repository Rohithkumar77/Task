""" Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?"""
def find_pairs_with_sum(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    
    return pairs

arr = [2, 7, 4, 5, 11, 9]
target = 9
result = find_pairs_with_sum(arr, target)
print(result)
