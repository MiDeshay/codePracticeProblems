def group_anagrams(strs)
    
    hash = {}
    
    strs.each do |str|
        sortedStr = str.chars.sort.join
        
        if (!hash[sortedStr])
            hash[sortedStr] = [str]
        else
            hash[sortedStr] << str
        end
    end
    
    arr = []
    hash.each_value do |val|
        arr << val
    end
    
    arr
end