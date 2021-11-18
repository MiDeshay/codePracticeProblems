# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    
    hash = {}
    
    nums.each_with_index do |num, i|
        
        ans = target - num
        
        if (hash[num])
            return [hash[num], i]
        else 
            hash[ans] = i
        end
            
    end
    
end