//Today we want to solve an algorithmic problem.
//We want to get an array of numbers, in which two of the numbers contained withn the array must add up to a a greater
//number. For example:
//lets say you have an array of ;[2,3,6,7,5,9] and two of the numbers (any) contained in the array must add upto to 15.
//if indeed two numbers in the array do add up to 15, the result will bring back true, if not it will bring back false.
//So how do we go about this? There are actually 2 methods, let's go through them.

function sum(arr, taskNo){
    for(i = 0; i < arr.length; i++){
        for(j = i+1; j < arr.length; j++){
            if(arr[i] + arr[j] === taskNo){
                return true
            }
        }
    }
    return false
}
let nums = [2,3,6,7,5,9]
console.log(sum(nums, 11))