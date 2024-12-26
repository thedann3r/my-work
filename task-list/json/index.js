let url = "http://localhost:3000/Marvel"
fetch(url)
.then(resp => resp.json())
.then(data => {
    data.forEach(movie => {
        displayMarvel(movie)
    })
})
.catch(err => console.log(err))

let head = document.getElementById("mainHead")
head.addEventListener("mouseover", () => {
    head.style.color = 'white'
})
head.addEventListener("mouseleave", () => {
    head.style.color = 'black'
})

      //For creating a new form.
let newMarvel = document.getElementById("add")
newMarvel.addEventListener("submit", (e) => {
    e.preventDefault()
    let newForm = new FormData(e.target)
    let newness = {
        Title:newForm.get("title"),
        id:newForm.get("id"),
        Image:newForm.get("image"),
        Starring:newForm.get("starring"),
        Release:newForm.get("release")
    }

    fetch(url, {
        method:"POST",
        headers:{
            'Content-Type' : "application/json"
        },
        body: JSON.stringify(newness)
    })
    .then(res => console.log(res))
    .then( movie => {
        alert(`${movie.Title} Created Successfully!`)
    })
    .catch(error => console.log(error))
})

let create = document.getElementById("create")
create.addEventListener("mouseover", () => {
    create.style.color = 'black'
    create.style.background = 'white'
    create.style.borderColor = 'black'
})
create.addEventListener("mouseleave", () => {
    create.style.color = 'white'
    create.style.background = 'black'
    create.style.borderColor = 'white'
})

   //For displaying the existing form.
function displayMarvel(movie){
    let movies = document.createElement("div")
    movies.classList.add("movies")
    movies.innerHTML = `
    <h3>${movie.Title}</h3>
    <img id= "image" src=${movie.Image}>
    <p>Starring: ${movie.Starring}</p>
    <p>Release: ${movie.Release}</p>
    <form id="edit" onsubmit="editForm(event,this,${movie.id})">
    <input class="editing" type="text" name="title" placeholder="Title" required><br>
    <input class="editing" type="url" name="image" placeholder="Image" required><br>
    <input class="editing" type="text" name="starring" placeholder="Starring" required><br>
    <input class="editing" type="number" name="release" placeholder="Release" required><br>
    <button id="ed">EDIT</button>
    <button id="butt" onclick="deleteMarvel(${movie.id})">REMOVE</button>
    `

let commentForm = document.createElement("form")
commentForm.id = "commentForm"
let comment = document.createElement("textarea")
comment.classList.add("comment")
comment.placeholder = "Add comment here..."
comment.name = "comment"
comment.required = "true"
let combutton = document.createElement("button")
combutton.classList.add("butt")
combutton.textContent = "ADD"
combutton.type = "submit"
commentForm.appendChild(comment)
commentForm.appendChild(combutton)

commentForm.addEventListener("submit", (e) => {
    e.preventDefault()
    let value = comment.value
    let commented = document.createElement("div")
    commented.classList.add("commented")
    let comments = document.createElement("p")
    comments.textContent = value
    commented.appendChild(comments)
    movies.appendChild(commented)
    let del = document.createElement("button")
    del.classList.add("del")
    del.textContent = "X"
    del.addEventListener("click", () => {
        del.parentNode.remove()
    })
    commented.appendChild(del)
    commentForm.reset()
})
movies.appendChild(commentForm)

    let movieContainer =document.getElementById("marvel-movies")
    movieContainer.appendChild(movies)
}

   //For deleting the a form.
function deleteMarvel(id){
    fetch(`${url}/${id}`,{
        method:"DELETE",
        headers:{
            'Content-Type' : "application/json"
        }
    })
    .then(resp => resp.json())
    .then( movie => {
        alert(`${movie.Title} Deleted Successfully`)
    })
    .catch(error => console.log(error))
}

function editForm(event,form,id){
    event.preventDefault()
    let editData = new FormData(form)
    let edited = {
        Title:editData.get("title"),
        Image:editData.get("image"),
        Starring:editData.get("starring"),
        Release:editData.get("release")
    }
    fetch(`${url}/${id}`, {
        method:"PATCH",
        headers:{
            'Content-Type' : "application/json"
        },
        body:JSON.stringify(edited)
    })
    .then(response => console.log(response))
    .then( movie => {
        alert(`${movie.Title} Edited Successfully!`)
    })
    .catch(err => console.log(err))
}

// let commentForm = document.createElement("form")
// commentForm.id = "commentForm"
// let comment = document.createElement("textarea")
// comment.classList.add("comment")
// comment.placeholder = "Add comment here..."
// comment.name = "comment"
// comment.required = "true"
// let combutton = document.createElement("button")
// combutton.classList.add("butt")
// combutton.textContent = "ADD"
// combutton.type = "submit"
// commentForm.appendChild(comment)
// commentForm.appendChild(combutton)

// commentForm.addEventListener("submit", (e) => {
//     e.preventDefault()
//     let value = comment.value
//     let commented = document.createElement("p")
//     commented.textContent = value
//     movies.appendChild(commented)
// })

// let create = document.getElementById("create")
// create.addEventListener("mouseover", () => {
//     create.style.color = 'black'
//     create.style.background = 'white'
//     create.style.borderColor = 'black'
// })
// create.addEventListener("mouseleave", () => {
//     create.style.color = 'white'
//     create.style.background = 'black'
//     create.style.borderColor = 'white'
// })

// let images = document.getElementById("image")
// images.addEventListener("mouseover", () => {
//     images.style.transform = "scale(0.9)"
// })

// images.addEventListener("mouseout", () => {
//     images.style.transform = "scale(1)"
// })