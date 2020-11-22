import React , {Component} from 'react';
import {Container, Jumbotron} from 'react-bootstrap';
import '../App.css';

export class Login_Jumbo extends Component{
    render(){
        return(
            <div>
                <Jumbotron fluid >
                <Container >
                    <h1>GetHub</h1>
                    <p>
                    The real anti-social social club
                    </p>
                </Container>
                </Jumbotron>
            </div>

        );
    }
}

export default Login_Jumbo;