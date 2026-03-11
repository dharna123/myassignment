import logo from './logo.svg';
import './App.css';
import {useEffect,useState} from "react"
import axios from "axios";
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import AddStudent from './AddStudent';
import Home from './Home';
import EditStudent from './EditStudent';
function App() {
return(
  <BrowserRouter>
  <Routes>
    <Route path="/" element={<Home></Home>}></Route>
    <Route path="/add" element={<AddStudent></AddStudent>}></Route>
    <Route path="/edit/:id" element={<EditStudent></EditStudent>}></Route>
  </Routes>
  
  </BrowserRouter>
)
}

export default App;
