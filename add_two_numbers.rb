# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    ptr = l1
    ptr2 = l2
   
    multiplier = 1
    
    sum1 = 0
    sum2 = 0
    
    while(ptr || ptr2)
        
        if ptr 
            num = ptr.val * multiplier
            sum1 += num
            ptr = ptr.next
        end
        
        if ptr2
            num2 = ptr2.val * multiplier
            sum2 += num2
            ptr2 = ptr2.next
        end
        
        multiplier *= 10
        
    end
    
    sum = sum1 + sum2
    
    arr = []
    
    sum.to_s().reverse.each_char do |char|
        arr.push(char.to_i)
    end

    return arr
    
end

#convert lists to numbers
#create two num vars set to 0
#set mutliplier = to 1
# look at the first number in each list
# multiply the number by the multiplier 
# add each number to a respsective sum

#if there is another number 
# look at that number
#increase the multiplier by 10x
#multiply the number by the multiplier
#add each number to a respective sum

#if there isn't another number
#add the two sums togther

#to get each number from the sum
#convert sum to string, reverse it, and get each char
#add char converted to an integer to an array

