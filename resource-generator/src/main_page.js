import React from 'react';
import MainCss from "./main_page.css";
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import AddResource from './Add_resource_page.js';

class MainPage extends React.Component {
  //This is the main page that contains a category bar, description bar and side bar. while the front part prompts the user to look for 
  //resources, the side bar will contain things like "Add Resource ", "Log out", "Terms of Services"
  //Below there's a skeleton code to show how the layout might be like although this one only contains a single search bar.
    render(){
        return ( 
          <Router>
          <div className ="MainPage">
            <label className ="hamburger-menu">
              <input type ="checkbox" />
            </label>
             <aside className = "sidebar">
              <nav>
                <div> 
                  <Link to="/AddResource" >Add Resource </Link> 
                </div>
                <div>Log out</div>
                <div>Terms of Services</div>
              </nav>  
              <Routes>
              <Route path="/AddResource" element={<AddResource />} />
              </Routes>
            </aside> 
            <div class= "main-part">
             <h1>  Welcome to Resource Generator for Wesleyan University! </h1>  
            <p> Please enter some keywords to check if there's a resource that could solve your problems. </p>      
            <form>
                <input type ="text" Placeholder = "Search..." name = "q" />
                <button type = "submit"> <img src = "Assets/search.png" /> </button>
            </form>
            </div>
        </div>
        </Router>)

    }
}   

export default MainPage;