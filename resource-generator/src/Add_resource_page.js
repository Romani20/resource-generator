import React from 'react';
import resourceCss from "./Add_resource_page.css";

class AddResource extends React.Component {
    //This is a page where users go to add resource. It takes information and a brief 
    //description about the resource a user wants to ass and updates the data base with the new resource. 
    //below there's a code to show what the general layout might look like. 
    render() {
        return ( 
            <div className= "AddResource">
                <h3>Hi! Are there any resources that you want to include? Please go ahead and enter the required infromation</h3>
                <input type= "text" placeholder ="Name of the Resouce" /> 
                <input type="text" placeholder = "Where can people access this resource" />
                <input type = "text" placeholder="Please give us a brief description of the resource" />
                <button> Submit </button>
            </div>
        )
    }
}
export default AddResource;