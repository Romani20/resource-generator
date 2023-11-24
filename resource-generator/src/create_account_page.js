// import React from 'react';
import React, { useState } from 'react';

const CreateAccount = () => {
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
    });

    const handleInputChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSignUp = () => {
        fetch('http://localhost:5000/create_account', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
    };

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

export default CreateAccount;

