    def minDepth(self, root: Optional[TreeNode]) -> int:
        
       
        res = float("inf")
        list = [(root, 1)]
        
        if not root:
            return 0
        
        while list: 
            node, depth = list.pop(0)
            
            if node:
                if not node.left and not node.right:
                    res = min(depth, res)
    
                if node.left:
                    list.append((node.left, depth + 1))
                if node.right:
                    list.append((node.right, depth + 1))
        return res