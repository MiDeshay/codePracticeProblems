const obj = {
    a: 1,
    b: 2,
    c: 3
}

for (const key in obj){
    //console.log(`${key}: ${obj[key]}`);
}

const arr = [1,2,3,4,5]

for (let i = 0; i < arr.length; i++){
    //console.log(arr[i])
}

arr.push("string", { d: 4})

//console.log(arr)

//arr.pop()

//console.log(arr.includes(4))

//console.log(arr.indexOf(4))

let string = "This is my sentence"

//console.log(string.split(' '))

// console.log(string.split("").sort().join(""))

// console.log(string.slice(0, 1))
// console.log(string.slice(1))


// arr.forEach((el, i) => {
//     console.log(el, i)
// })

// string.forEach(char => {
//     console.log(char)
// })
