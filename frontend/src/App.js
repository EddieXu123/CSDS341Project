import './App.css';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavigationBar from './components/NavigationBar';
import Login from './components/Login';
import Login_Jumbo from './components/Login_Jumbo';


function App() {
  return (
    <div>
      <NavigationBar/>
      <Login_Jumbo/>
      <Login/>
      
    </div>
  );
}

export default App;
