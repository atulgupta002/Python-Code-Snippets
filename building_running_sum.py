#Function to create a running sum (prefix array) of a 1D list nums
def running_sum(nums):
  assert isinstance(nums,list)
  
  n = len(nums)
  
  if n == 0:
    return []
  
  running_sum = [nums[0]]
  
  for i in range(1,n):
    running_sum.append(nums[i] + running_sum[len(running_sum) - 1])
  
  return running_sum
