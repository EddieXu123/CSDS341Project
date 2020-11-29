import React , {Component} from 'react';
import {Navbar, Nav, Form, NavDropdown, FormControl, Button} from 'react-bootstrap';
import '../App.css';

export class Register extends Component{
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
                <Form.Group controlId="formGroupPasswordTwo">
                    <Form.Label>Re enter Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>

                <Form.Group controlId="formGroupPasswordTwo">
                    <Form.Label>Personal Information</Form.Label>
                    <Form.Control type="text" placeholder="First Name" />
                    <Form.Control type="text" placeholder="Last Name" />
                    <Form.Control type="text" placeholder="DOB DD/MM/YYYY" />
                </Form.Group>

                <Form.Group>
                <Button variant="primary" type="submit" class="login_button">
                    Login
                </Button>
                </Form.Group>
                </Form>oka
            </div>
        );
    }
}

export default Register;
