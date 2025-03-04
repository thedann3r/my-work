import { useEffect, useState } from 'react'
import './App.css'
import RiversList from './RiversList'
import NewRiver from './NewRiver'

function App() {
  const [rivers, setRivers] = useState([])
  useEffect(()=>{
    fetch("http://127.0.0.1:5000/rivers")
    .then(res => res.json()) 
    .then(data =>{
      setRivers(data)
    })
  },[])

  return (
    <>
      <h1>This is the rivers page</h1>
      <RiversList rivers = {rivers} setRivers = {setRivers} />
      <NewRiver rivers = {rivers} setRivers = {setRivers} />
    </>
  )
}

export default App
