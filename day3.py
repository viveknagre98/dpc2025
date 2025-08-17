def findDuplicate(nums):
  slow = nums[0]
  fast = nums[0]
 while True:
   slow = nums[slow]
   fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
return slow
print(findDuplicate([1, 3, 4, 2, 2]))   
print(findDuplicate([3, 1, 3, 4, 2]))       
print(findDuplicate([1, 1]))                
print(findDuplicate([1, 4, 4, 2, 3]))       
print(findDuplicate(list(range(1, 100000)) + [50000])) 
