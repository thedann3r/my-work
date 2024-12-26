import { Link } from "react-router-dom"
function Header() {

    return (
      <>
      <div>
        <nav>
            <Link to={"/"}>App</Link>
            <Link to={"/home"}>Home</Link>
            <Link to={"/about"}>About</Link>
            <Link to={"/contacts"}>Contacts</Link>
        </nav>
      </div>
      </>
    )
  }
  
  export default Header