class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) == 2):
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        if (len(nums) == 1):
            return [[nums[0]]]
        
        curr = nums[0]
        
        perms = self.permute(nums[1:])
        
        
        arr = []
        for perm in perms:
            for i in range(len(nums)):
                arr.append(perm[0:i] + [curr] + perm[i: ])
            
        return arr
            