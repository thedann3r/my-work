import { useState } from 'react'

function LoginForm() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault();
    const credentials = { username, password }

    // Send credentials to backend for authentication
    fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(credentials),
    })
    .then(res => res.json())
    .then(data => {
      if (data.token) {
        // If a token is received, store it (localStorage or state)
        localStorage.setItem('authToken', data.token)
        console.log('Login successful')
      } else {
        console.log('Login failed')
      }
    })
    .catch(err => console.error(err))
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
      </label>
        <input type="text"   value={username} onChange={(e) => setUsername(e.target.value)} />
      <label>
        Password:
      </label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Login</button>
    </form>
  )
}

export default LoginForm
