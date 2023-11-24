// import React from 'react';
import signInCss from './sign-In.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CreateAccount from './create_account_page.js';
import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';

const AuthContext = React.createContext();

const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const login = () => {
        // Perform login logic (e.g., send a request to the Flask backend)
        // Update isAuthenticated state accordingly
        setIsAuthenticated(true);
    };

    const logout = () => {
        // Perform logout logic (e.g., send a request to the Flask backend)
        // Update isAuthenticated state accordingly
        setIsAuthenticated(false);
    };

    return (
        <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

const useAuth = () => {
    return useContext(AuthContext);
};

const SignInPage = () => {
    const { login } = useAuth();
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });
    const history = useHistory();

    const handleInputChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSignIn = () => {
        // Send a request to the Flask backend to check credentials and log in
        // Update the login function to communicate with your backend
        login();
        history.push('/main'); // Redirect to the main page after successful login
    };{
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