# a 'profit' occurs anytime the current price is greater than the price before it
# adding all the differences between the current price and the price from the day before in that case
# produces the correct answer

def max_profit(prices)
    profit = 0
    
    prices.each_with_index do |price, i|
        if i > 0 
             if price > prices[i - 1]
                profit += price - prices[i - 1]  
             end
        end
    end
    
    return profit
    
end