import React from 'react';
import signUpCss from './sign-in.css';


class SignUpPage extends React.Component {
    //This is a page the user will see when they open Resource genrator for the first time.
    //It'll ask them to create an account if they don't have one or to login if they already do. 
    //The code below shows a simple/plain implementation of this
    render(){
        return (
            <div className="SignUpPage">
              <h1> Welcome </h1>
                <form>
                    <input type ="email" class= "input-box" placeholder = "Your Email">
                    </input> <br />
                    <input type ="Password" class= "input-box" placeholder = "Your Password">
                    </input> <br />
                    <button type ="button" class = "signup-btn"> Sign up </button>
                </form>
        </div> )
        }
}
export default SignUpPage;