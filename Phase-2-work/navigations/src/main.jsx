import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { createBrowserRouter,RouterProvider } from 'react-router-dom'
import Layout from './Layout.jsx'
import Home from './Home.jsx'
import About from './About.jsx'
import Contacts from './Contacts.jsx'

const router = createBrowserRouter([
  {
    path:"/",
    element:<Layout />,
    children:[
      {
        path:"/",
        element:<App />
      },
      {
        path:"/home",
        element:<Home />
      },{
        path:"/about",
        element:<About />
      },{
        path:"/contacts",
        element:<Contacts />
      }
    ]
  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
