import { useState } from "react"

function RiversItems({name, source, length_in_km, id, rivers, setRivers}){
    const[updateRiver, setUpdateRiver] = useState({
        name: '',
        source:"",
        length_in_km:0
    })
    function handleChange(e){
        const {name, value} = e.target

        setUpdateRiver({
            ...updateRiver,
            [name]:value
        })
    }
    function handleUpdate(e){
        e.preventDefault()
        fetch(`http://127.0.0.1:5000/rivers/${id}`,{
            method: 'PATCH',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(updateRiver)
        })
        .then(resp => resp.json())
        .then(updated =>{
            let updateRiver = rivers.map(river => {
                if(river.id === id){
                    river.name = updated.name
                    river.source = updated.source
                    river.length_in_km = updated.length_in_km
                }
                return river
            })
            setRivers(updateRiver)
            setUpdateRiver({
                name: '',
                source:"",
                length_in_km:0
            })
            alert(`The river ${updated.name}, has been updated successfully!`)
        })
    }

function handleDelete(e){
    e.preventDefault()
    fetch(`http://127.0.0.1:5000/rivers/${id}`,{
        method: 'DELETE',
        headers: {
            'Content-Type':'application/json'
        }
    })
    .then(res => res.json())
    .then(() =>{
        const remain = rivers.filter(river => river.id !== id)
        setRivers(remain)
        alert(`The river ${name}, has been deleted successfuly!`)
    })
}

    return(
        <>
        <div className="river-items">
           <h1>{name}</h1>
           <h2>{source}</h2>
           <h3>{length_in_km}</h3>  

           <form onSubmit={handleUpdate}>
            <input type="text" name="name"  placeholder="name..." required value={updateRiver.name} onChange={handleChange}/><br />
            <input type="text" name="source"  placeholder="source..."  required value={updateRiver.source} onChange={handleChange}/><br />
            <input type="number" name="length_in_km"  placeholder="length..." required value={updateRiver.length_in_km} onChange={handleChange}/> <br />
            <button>Update!</button>
          </form>    

           <button onClick={handleDelete}>Delete!</button> 
        </div>
        </>
    )
}

export default RiversItems