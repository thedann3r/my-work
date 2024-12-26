let form = document.getElementById("squad")
form.addEventListener("submit", (e) => {
    e.preventDefault()
    let value = document.getElementById("players").value
    let list = document.getElementById("list")
    let items = document.createElement("li")
    items.textContent = value
    list.appendChild(items)
    let button = document.createElement("button")
    button.textContent = "X"
    button.style.marginLeft = "10px"
    button.addEventListener("click", () => {
button.parentNode.remove()
    })
    items.appendChild(button)
    form.reset()
})
