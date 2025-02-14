// function add(num1, num2, num3){
//     return num1 + num2 + num3;
// }
// console.log(add(2,3,4))

// const names = ["Dann","Christopher","Dorothy","Stephen"]
// names.forEach(jina =>{
//     console.log(jina)
// })

// for(let name of names){
//     console.log(name)
// }

// const names = ["Dann","Christopher","Dorothy","Stephen"]
// let startsD = names.filter((students) => {
//     return students.startsWith("D")
// })
// console.log(names)
// console.log(startsD)

// const names = ["Dann","Christopher","Dorothy","Stephen"]
// let startsD = names.find((students) => {
//     return students.startsWith("C")
// })
// console.log(names)
// console.log(startsD)

// const numbers = [12,34,25,16]
// let product = numbers.reduce((accumumulator, num) => {
//     return accumumulator * num
// },1)
// console.log(product)

// let nums = [1,2,3,6,5]
// let num = nums.map(number => number * 2)
// let numb = num.filter(numbe => numbe >= 5)
// console.log(numb)

// let i = 0
// while(i <= 10){
//     console.log(i)
//     i++
// }

// for(let i = 0; i <= 10; i++){
//     console.log(i)
// }

// let age = 1
// let result = age >=18 ? "You are an adult!" : "You are still a child!"

// console.log(result)

// let number = 7
// let result = number % 2 === 0 ? "An even number" : "An odd number"

// console.log(result)

//Convert digit into Roman numeros

function romans(R){
    let romanNumero = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',}
    let result = ''

    if(R >= 1000){
        let count = Math.floor(R / 1000)
        result += romanNumero[1000].repeat(count)
        R -= count * 1000
    }
    if(R >= 500){
        let count = Math.floor(R / 500)
        result += romanNumero[500].repeat(count)
        R -= count * 500
    }
    if(R >= 100){
        let count  = Math.floor(R / 100)
        result += romanNumero[100].repeat(count)
        R -= count * 100
    }
    if(R >= 50){
        let count  = Math.floor(R / 50)
        result += romanNumero[50].repeat(count)
        R -= count * 50
    }
    if(R >= 10){
        let count  = Math.floor(R / 10)
        result += romanNumero[10].repeat(count)
        R -= count * 10
    }
    if(R >= 5){
        let count  = Math.floor(R / 5)
        result += romanNumero[5].repeat(count)
        R -= count * 5
    }
    if(R >= 1){
        let count  = Math.floor(R / 1)
        result += romanNumero[1].repeat(count)
        R -= count * 1
    }

    return result
}
console.log(romans(4321))
