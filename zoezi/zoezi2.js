function greetings(callback){
    const greet = ["Hello", "good morning"]
    console.log(greet.join(" "))
    setTimeout(function(){
        callback()
    },2500)
}
function received(){
    console.log("Good morning to you too!")
}
greetings(received)

