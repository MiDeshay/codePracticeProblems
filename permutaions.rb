#think of dealing cards

def permute(nums)
    return [[nums.first]] if nums.length == 1
    return [nums, nums.reverse] if nums.length == 2
    
    firstEl = nums.first
    rest = nums[1..-1]
    
    perms = permute(rest)
    
    arr = []
  
    perms.each do |perm|
       (0..perm.length).each do |i|
         left = perm.slice(0,i)
         right = perm.slice(i, perm.length)
           
         result = nil
      
        result = left + [firstEl] + right 
         
          
           
         arr << result
        end
    end
    
    arr
end

p permute([5,4,6,2])



#if array length is one, return first el in an array

#if array length is two, return the array and its reverse

#else

#take first el from array, call permute on the remainder
#insert first element into each position of result and push it to an array

#return array


