def climb_stairs(n, memo=Hash.new)
    
    return 1 if n == 0
    return 0 if n == -1
    return memo[n] if memo.has_key?(n)

    memo[n] = climb_stairs(n-1, memo) + climb_stairs(n-2, memo) 
    

end