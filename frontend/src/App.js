import './App.css';
import React , {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavigationBar from './components/NavigationBar';
import Login from './components/Login';
import LoginPage from './components/LoginPage';
import Login_Jumbo from './components/Login_Jumbo';
import { Register } from './components/register';
import {BrowserRouter as Router, Route, Switch, Link, Redirect} from "react-router-dom";

class App extends Component{
  render(){
    return(
      <Router>
        <Switch>
        <Route exact path = "/" component ={LoginPage}></Route>
        <Route exact path = "/Register" component ={Register}></Route>
        </Switch>
      </Router>
    )
  }
}

export default App;
