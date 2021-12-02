class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        last = nums[-1]
      
        
        
        subs = self.subsets(nums[0: -1])
        
        result = subs.copy()
        
        
        for el in subs:
            
            if len(el) > 0:
                result.append([*el, last])
            else: 
                result.append([last])
                
        return result

        