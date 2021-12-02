# [-2,1,-3,4,-1,2,1,-5,4]

# -2 -> 1 

# sum 1 is positive so save sum and keep going
# if this sum is greater than the max sum, replace it


# -2 -> 1 -> -3 

#sum -1 is negative so, set sum to 0 and keep going


# -2 -> 1 -> -3  sum now 0 -> 4

# sum 0 + 4 = 4 is positive and greater than prev sum so it replaces max sum and keeps going


'''
1. initailize sum = 0 and max_sum = 0 variables
2. iterate through the array adding sum to current element and saving result to sum
3. if sum is greater than max_sum, set max_sum = sum
4.  if sum is negative, set sum to 0
5. after loop, return max sum

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_sum = 0
        max_sum = float("-inf")
        
        for num in nums:
            local_sum = local_sum + num
            
            if local_sum > max_sum:
                max_sum = local_sum
            
            if local_sum < 0:
                local_sum = 0
                
        return max_sum