import { useEffect, useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from "react-router-dom"
import './App.css'

const url = "http://127.0.0.1:5000"

function App() {
    const [user, setUser] = useState(null)
    const [products, setProducts] = useState([])
    const [users, setUsers] = useState([])
    const [token, setToken] = useState(localStorage.getItem('access_token'))

    useEffect(() => {
        if (token) {
            fetchProducts()
            if (user?.role === "admin") {
                fetchUsers()
            }
        }
    }, [token, user])

    const fetchProducts = () => {
        fetch(`${url}/products`, {
            headers: { Authorization: `Bearer ${token}` },
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                }
                throw new Error('Failed to fetch products')
            })
            .then((data) => {
                setProducts(data)
            })
            .catch((error) => {
                console.error('Error fetching products:', error)
            })
    }

    const fetchUsers = () => {
        if (user?.role !== 'admin') {
            window.location.href = "/products"
            return
        }

        fetch(`${url}/users`, {
            headers: { Authorization: `Bearer ${token}` },
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                } else {
                    console.error('Error fetching users:', response.statusText)
                    throw new Error('Error fetching users')
                }
            })
            .then((data) => {
                setUsers(data)
            })
            .catch((error) => {
                console.error('Error fetching users:', error)
            })
    }

    const handleLogin = (e) => {
        e.preventDefault()
        const formData = new FormData(e.target)

        fetch(`${url}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username: formData.get('username'),
                password: formData.get('password')
            }),
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                } else {
                    alert("Invalid credentials")
                    throw new Error('Invalid credentials')
                }
            })
            .then((data) => {
                setToken(data.access_token)
                setUser({ username: data.username, role: data.role })
                localStorage.setItem("access_token", data.access_token)
            })
            .catch((error) => {
                console.error("Login error:", error)
            })
    }

    const handleSignup = (e) => {
        e.preventDefault()
        const formData = new FormData(e.target)

        fetch(`${url}/signup`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username: formData.get('username'),
                password: formData.get('password'),
                role: formData.get('role') || 'user'
            }),
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                } else {
                    alert("Error signing up")
                    throw new Error('Error signing up')
                }
            })
            .then((data) => {
                setToken(data.access_token)
                setUser({ username: data.username, role: data.role })
                localStorage.setItem("access_token", data.access_token)
                
                if (data.role === 'user') {
                  alert("You have successfully signed up as a user")
              } else if (data.role === 'admin') {
                  alert("You have successfully signed up as an admin")
              } else{
                alert("Only a user or an admin can sign up!")
              }
              
            })
            .catch((error) => {
                console.error("Signup error:", error)
            })
    }

    const handleLogout = () => {
        setToken(null)
        setUser(null)
        localStorage.removeItem("access_token")
    }

    return (
        <Router>
            <nav>
                <Link to="/products">Products</Link>
                {user?.role === 'admin' && <Link to="/users">Users</Link>}
                {user ? (
                    <button onClick={handleLogout}>Logout</button>
                ) : (
                    <>
                        <Link to="/login">Login</Link>
                        <Link to="/signup">Signup</Link>
                    </>
                )}
            </nav>
            <Routes>
                <Route path="/products" element={token ? <Products products={products} /> : <Navigate to="/login" />} />
                <Route path="/users" element={user?.role === 'admin' ? <Users users={users} /> : <Navigate to="/products" />} />
                <Route path="/login" element={user ? <Navigate to="/products" /> : <LoginForm handleLogin={handleLogin} />} />
                <Route path="/signup" element={user ? <Navigate to="/products" /> : <SignupForm handleSignup={handleSignup} />} />
            </Routes>
        </Router>
    )
}

function Products({ products }) {
    return (
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

function Users({ users }) {
    return (
        <div>
            <h2>Users</h2>
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

function LoginForm({ handleLogin }) {
    return (
        <form onSubmit={handleLogin}>
            <input type="text" name="username" placeholder="Enter username..." required />
            <input type="password" name="password" placeholder="Enter password..." required />
            <button type="submit">Login</button>
        </form>
    )
}

function SignupForm({ handleSignup }) {
    return (
        <form onSubmit={handleSignup}>
            <input type="text" name="username" placeholder="Enter username..." required />
            <input type="password" name="password" placeholder="Enter password..." required />
            <input type="text" name="role" placeholder="Enter role (optional)" />
            <button type="submit">Sign Up</button>
        </form>
    )
}

export default App
