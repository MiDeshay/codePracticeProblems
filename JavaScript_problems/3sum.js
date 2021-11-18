var threeSum = function(nums) {
    
    const res = []
    
    nums.sort(sortNumber)
    
    nums.forEach((num, i) => {
        if(i > 0 && num == nums[i -1]){
            return
        }
        
        let lpt = i + 1
        let rpt = nums.length - 1
        
        while (lpt < rpt){
        
            let threesome = num + nums[lpt] + nums[rpt]
    
            if (threesome > 0){
                rpt -= 1
            } else if (threesome < 0){
                lpt += 1
            } else {
                const sum = [num, nums[lpt], nums[rpt]]
                res.push(sum) 
                lpt +=1
                
                while (nums[lpt] === nums[lpt -1] && lpt < rpt){
                    lpt += 1
                }
            }
        }
    })
return res
};

function sortNumber(a, b) {
   return a - b;
}