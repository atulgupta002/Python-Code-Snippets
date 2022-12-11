def valid_splits(nums):
  assert isinstance(nums,list)
  
  prefix = [nums[0]]
  ans = 0
  
  #building prefix array
  for i in range(1,len(nums)):
    prefix.append(nums[i] + prefix[len(prefix) - 1])
    
  for i in range(len(prefix) - 1):
    left = prefix[i]
    right = prefix[len(prefix) - 1] - left
    
    if left >= right:
      ans += 1
  return ans
