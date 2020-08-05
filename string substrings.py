from itertools import combinations 
  
# initializing string  
test_str = "leetcode"
  
# printing original string  
print("The original string is : " + str(test_str)) 
  
# Get all substrings of string 
# Using itertools.combinations() 
res = [test_str[x:y] for x, y in combinations( 
            range(len(test_str) + 1), r = 2)] 
  
# printing result  
print(res)
