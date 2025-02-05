import { useEffect, useState } from 'react'
import './App.css'
// import RiversList from './RiversList'
// import NewRiver from './NewRiver'
import LoginForm from './New'

function App() {
  const [rivers, setRivers] = useState([])
  useEffect(()=>{
    fetch("http://127.0.0.1:5000")
    .then(res => res.json()) 
    .then(data =>{
      setRivers(data)
    })
  },[])

  return (
    <div>
      <h1>Login</h1>
      <LoginForm />
    </div>
  )
}

export default App
