import React from 'react';
import MainCss from "./main_page.css";

class MainPage extends React.Component {
    render(){
        return ( 
            <div className ="MainPage">
                <header>
      <div class="logo">
        <img src="" />
      </div>
      <button class="nav-toggle" aria-label="toggle navigation">
        <span class="hamburger"> </span>
      </button>
      <nav class="nav">
        <ul class="nav__list">
          <li class="nav__item"><a href="#" class="nav__link"> Home </a></li>
          <li class="nav__item">
            <a href="#" class="nav__link"> What I do </a>
          </li>
          <li class="nav__item">
            <a href="#" class="nav__link"> About me </a>
          </li>
          <li class="nav__item"><a href="#" class="nav__link"> My work </a></li>
        </ul>
      </nav>
    </header>
             <h1>  Welcome to Resource Generator for Wesleyan University! </h1>  
            <p> Please enter some keywords to check if there's a resource that could solve your problems. </p>      
            <form>
                <input type ="text" Placeholder = "Search..." name = "q" />
                <button type = "submit"> <img src = "Assets/search.png" /> </button>
            </form>
        </div>
        )

    }
}   

export default MainPage;