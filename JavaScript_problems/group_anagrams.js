var groupAnagrams = function(strs) {
    const obj = {}
    
    strs.forEach(str => {
        const sortedString = str.split("").sort().join("")
        
        if (!obj[sortedString]){
            obj[sortedString] = [str]
        } else {
            obj[sortedString].push(str)
        }
    })
    
    const arr = []
    for (const key in obj){
        arr.push(obj[key])
    }
    
    return arr
};