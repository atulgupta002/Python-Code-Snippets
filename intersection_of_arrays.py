#Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
# Hashmap usage and example.

def intersection(nums):
  output = []
  map = {}
  n = len(nums)
  
  for array in nums:
    for item in array:
      if item in map:
        map[item] += 1
      else:
        map[item] = 1
      if map[item] == n:
        output.append(item)
   output.sort()
  return output
