# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Time-Complexity: O(n)

def sorted_squares(nums):
  p1 = 0
  p2 = len(nums) - 1
  result = []
  for i in range(p2,-1,-1):
    temp = 0
    if abs(nums[p1]) < abs(nums[p2]):
      temp = abs(nums[p2])
      p2 -= 1
    else:
      temp = abs(nums[p1])
      p1 += 1
    result = [temp * temp] + result
  return result
      
