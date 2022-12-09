# Function to reverse a list in-place using O(1) memory. Demonstration of the two-pointer method. Time-complexity: O(n)

def swap(a,b):
  temp = a
  a = b
  b = temp
  return

def reverse(s):
  assert isinstance(s,list)
  p1 = 0
  p2 = len(s)
  while p1 < p2:
    swap(s[p1],s[p2])
    p1 += 1
    p2 -= 1
