import React , {Component} from 'react';
import {Navbar, Nav, Form, NavDropdown, FormControl, Button} from 'react-bootstrap';
import '../App.css';

export class NavigationBar extends Component{
    render(){
        return(
            <div>
                <Navbar bg="light" expand="lg">
                <Navbar.Brand href="#home">GetHub</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                    <Nav.Link href="/">Home</Nav.Link>
                    <Nav.Link href="#link">About Us</Nav.Link>
                    </Nav>
                    <Button variant="outline-success" href="/Register">Register</Button>
                </Navbar.Collapse>
                </Navbar>
            </div>

        );
    }
}

export default NavigationBar;


