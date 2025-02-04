// push (destructive)
// let numbers = [1,2,3,4,5]
// numbers.push(6)
// console.log(numbers)

// unshift (destructive)
// let numbers = [2,3,4,5,6]
// numbers.unshift('one')
// console.log(numbers)

// spread (non-destructive)
// let numbers = [1,2,3,4,5]
// let newDigits = [0,...numbers,6]
// console.log(numbers)
// console.log(newDigits)

// pop (destructive)
// let numbers = [1,2,3,4,5]
// numbers.pop()
// console.log(numbers)

// shift (destructive)
// let numbers = [1,2,3,4,5]
// numbers.shift()
// console.log(numbers)

// slice (non-destructive)
// let numbers = [1,2,3,4,5,6,7,8,9,10]
// let sliced = numbers.slice(2,7)
// console.log(sliced)
// console.log(numbers)

// splice (destructive)
// array.splice(startIndex, deleteCount, item1, item2, ...)
let numbers = [1,2,3,4,5,6,7,8,9,10]
let spliced = numbers.splice(2,3,11,12,13)
console.log(numbers)
console.log(spliced)