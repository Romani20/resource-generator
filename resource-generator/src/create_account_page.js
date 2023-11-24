import React from 'react';
class CreateAccount extends React.Component { 
    render(){
        return (
            <div className="CreateAccount">
            <h1> Welcome </h1>
            <form>
                    <input type ="text" class= "input-box" placeholder = "First Name">
                    </input> <br />
                    <input type ="email" class= "input-box" placeholder = "Last Name">
                    </input> <br />
                    <input type ="email" class= "input-box" placeholder = "Your Email">
                    </input> <br />
                    <input type ="Password" class= "input-box" placeholder = "Your Password">
                    </input> <br />
                    <input type ="Password" class= "input-box" placeholder = "Confirm Password">
                    </input> <br />
                    <button type ="button" class = "signup-btn"> Sign Up </button>
            </form>
            </div>
            )

        }
    }

export default CreateAccount;

