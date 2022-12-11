#Function to check if a given string is a pangram. A pangram is a sentence/string that contains all the letters of the alphabet.
# Assumptions: 1. The string contains only letters and spaces.

def check_pangram(sentence):
  set_str = set(sentence);
  
  if len(set_str) == 26:
    return True
  return False
