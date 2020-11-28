import React , {Component} from 'react';
import {Navbar, Nav, Form, NavDropdown, FormControl, Button} from 'react-bootstrap';
import '../App.css';
import Login from './Login';
import Login_Jumbo from './Login_Jumbo';
import NavigationBar from './NavigationBar';

export class LoginPage extends Component{
    render(){
        return(
            <div>
                <NavigationBar/>
                <Login_Jumbo/>
                <Login/>

            </div>
        );
    }
}

export default LoginPage;