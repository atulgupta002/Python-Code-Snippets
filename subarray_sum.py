# Function to find the total number of subarrays in a list such that the sum of elements of subarray = k
# Introduction to defaultdict object.

from collections import defaultdict

def subarray_sum(nums,k):
  counts = defaultdict(int)
  counts[0] = 1
  
  ans = curr = 0
  
  for num in nums:
    curr += num
    ans += counts[k - num]
    counts[curr] += 1
  
  return ans
