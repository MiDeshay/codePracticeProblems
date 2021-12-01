class Solution:
    def __init__(self):
        self.hash_map = {}
        
    def climbStairs(self, n: int) -> int:
            
        if n == 0:
            return 1
        if n == -1:
            return 0
        
        if n not in self.hash_map:
            self.hash_map[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
        return self.hash_map[n]
        