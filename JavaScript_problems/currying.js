function compose (a, b){
    return function (x){
        return a(b(x))
    }
}

function a (num) {
    return num * 2
}

function b (x){
    return x + 3
}

console.log(compose(a,b)(5))