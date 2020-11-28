import React , {Component} from 'react';
import {Navbar, Nav, Form, NavDropdown, FormControl, Button} from 'react-bootstrap';
import '../App.css';
import Login_Jumbo from './Login_Jumbo';
import NavigationBar from './NavigationBar';

export class Login extends Component{
    render(){
        return(
            <div class="login">
                <Form>
                <Form.Group controlId="formGroupEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                </Form.Group>
                <Form.Group controlId="formGroupPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>

                <Form.Group>
                <Button variant="primary" type="submit" class="login_button">
                    Login
                </Button>
                </Form.Group>
                </Form>
            </div>
        );
    }
}

export default Login;