import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(100)

  return (
    <>
       <h1>{count}</h1>
      <button onClick={() => setCount((count) => count +1)}>increase</button>
      <button onClick={() => setCount((count) => count -1)}>decrease</button>
    </>
  )
}

export default App
