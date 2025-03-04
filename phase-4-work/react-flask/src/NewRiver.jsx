import { useState } from "react"

function NewRiver({rivers, setRivers}){
    const[newRiver, setNewRiver] = useState({
        name: "",
        source: "",
        length_in_km: 0
    })
    function handleChange(e){
        const name = e.target.name
        const value = e.target.value

        setNewRiver({
            ...newRiver,  
            [name]:value
        })
    }
    function handleSubmit(e){
        e.preventDefault()
        fetch("http://127.0.0.1:5000/rivers",{
            method: 'POST',
            headers:{
                "Content-Type":'application/json'
            },
            body:JSON.stringify(newRiver)
        })
        .then(res => res.json())
        .then(river => {
            setRivers([...rivers, river])
            setNewRiver({
                name: "",
                source: "",
                length_in_km: 0
            })
            alert (`The river ${newRiver.name}, has been created successfully!`)
        })
    }

    return(
        <>
          <form onSubmit={handleSubmit}>
            <input type="text" name="name"  placeholder="name..." required value={newRiver.name} onChange={handleChange}/>
            <input type="text" name="source"  placeholder="source..."  required value={newRiver.source} onChange={handleChange}/>
            <input type="number" name="length_in_km"  placeholder="length..." required value={newRiver.length_in_km} onChange={handleChange}/> <br />
            <button>Create!</button>
          </form>
        </>
    )
}

export default NewRiver