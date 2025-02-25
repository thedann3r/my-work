import { useEffect, useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from "react-router-dom"
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const url = "http://127.0.0.1:5000"

function App() {
    const [user, setUser] = useState(null)
    const [products, setProducts] = useState([])
    const [users, setUsers] = useState([])
    const [token, setToken] = useState(localStorage.getItem('access_token'))

    useEffect(() => {
      if(token){
        fetchProducts()
        if(user?.role ==="admin") {
          fetchUsers()
        }
      }
    }, [token, user])

    const fetchProducts = async () => {
      try{
        const response = await fetch(`${url}/products`, {
          headers: {Authorization:`Bearer ${token}` },
        })
        if(response.ok){
          const data = await response.json()
          setProducts(data)
        }
      }catch(error){
        console.error('Error fetching products:', error)
      }
    }

    const fetchUsers = async () => {
      if (user?.role !== 'admin') {
        // Redirect non-admin users away from the `/users` page
        window.location.href = "/products"; // Or use React Router's `Navigate`
        return;
      }
      try{
        const response = await fetch(`${url}/users`, {
          headers: {Authorization: `Bearer ${token}` },
        })
        if(response.ok){
          const data = await response.json()
          setUsers(data)
        }
        else {
          // Handle the case where the response is not okay (e.g., Forbidden or Unauthorized)
          console.error('Error fetching users:', response.statusText);
      }
     }catch(error){
        console.error('Error fetching products:', error)
      }
    }

    const handleLogin = async(e) => {
      e.preventDefault()
      const formData = new FormData(e.target)
      try{
        const response = await fetch(`${url}/login`, {
          method : 'POST',
          headers: {'Content-Type':'application/json'},
          body: JSON.stringify({
            username: formData.get('username'),
            password: formData.get('password')
          }),
        })
        if(response.ok){
          const data = await response.json()
          setToken(data.access_token)
          setUser({username: data.username, role: data.role})
          localStorage.setItem("access_token", data.access_token)
        }
        else{
          alert("Invalid credentials")
        }
      }
      catch(error){
        console.error("Login error:", error)
      }
    }

    const handleLogout = () => {
      setToken(null)
      setUser(null)
      localStorage.removeItem("access_token")
    }

    return(
    <Router >
      <nav>
        <Link to="/products">Products</Link>
        {user?.role === 'admin' && <Link to="/users">Users</Link>}
        {user ? (
          <button onClick={handleLogout}>Logout</button>
        ) : (
          <Link to="/login">Login</Link>
        )}
      </nav>
      <Routes>
        <Route path="/products" element={token ? <Products products={products} /> : <Navigate to="/login" />} />
        <Route path="/users" element={user ?.role === 'admin' ? <Users users={users} /> : <Navigate to="/products" />}/>
        <Route path="/login" element={user ? <Navigate to="/products" /> : <LoginForm  handleLogin={handleLogin}/>}/>
      </Routes>
    </Router>
    )
}

function Products({products}){
  return(
    <div>
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>{product.name}</li>
        ))}
      </ul>
    </div>
  )
}

function Users({users}){
  return(
    <div>
      <h2>users</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.username} - {user.role}
            </li>
        ))}
      </ul>
    </div>
  )
}
  
function LoginForm({handleLogin}){
    return(
      <form onSubmit={handleLogin}>
        <input type="text"  name='username' placeholder='enter username...' required/>
        <input type="password"  name='password' placeholder='enter password...' required/>
        <button type='submit'>Login</button>
      </form>
    )
  }

export default App