
def subsets(nums):
    if len(nums) == 1:
        return [[], [nums[0]]]
    
    last = nums[-1]
    
    
    
    subs = subsets(nums[0: -1])
    
    result = list(subs)
    
    
    for el in subs:
        
        if len(el) > 0:
            result.append(el + [last])
        else: 
            result.append([last])
            
    return result

        