import React from 'react';
import signInCss from './sign-in.css';


class SignInPage extends React.Component {
    render(){
        return (
            <div className="SignInPage">
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
export default SignInPage;