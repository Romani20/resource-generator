import React from 'react';
import signInCss from './sign-In.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CreateAccount from './create_account_page.js';


class SignInPage extends React.Component {
    //This is a page the user will see when they open Resource genrator for the first time.
    //It'll ask them to create an account if they don't have one or to login if they already do. 
    //The code below shows a simple/plain implementation of this
    render(){
        return (
          <Router>
            <div className="SignInPage">
              <h1> Welcome </h1>
                <form>
                    <input type ="email" class= "input-box" placeholder = "Your Email">
                    </input> <br />
                    <input type ="Password" class= "input-box" placeholder = "Your Password">
                    </input> <br />
                    <button type ="button" class = "signup-btn"> Sign In </button>
                    <p> New User?</p>
                    <nav>
                    <div> 
                    <a href="/CreateAccount" target="_blank">Create an account</a>
                    </div>
                    </nav>  
              <Routes>
              <Route path="/CreateAccount" element={<CreateAccount />} />
              </Routes>
              </form>
              </div>
              </Router>
           )
        }
}

export default SignInPage;