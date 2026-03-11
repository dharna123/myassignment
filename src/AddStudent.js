
import { useState } from "react"
import axios from "axios"
import { useNavigate } from "react-router-dom"




function AddStudent() {
const [formData,setFormData]=useState({name:"",age:"",course:""})
const navigate=useNavigate()
  
  const handleChange=(e)=>{

    setFormData({
      ...formData,[e.target.name]:e.target.value
    })



  }

  const addStudent=()=>{
axios.post("http://localhost:5000/students",formData)
.then(()=>{
    navigate("/")
  
})
  }




  
  return (
 <>
 
 <input  name="name" value={formData.name} onChange={handleChange}></input>
 <input  name="age" value={formData.age} onChange={handleChange}></input>
 <input name="course" value={formData.course} onChange={handleChange}></input>
 <button onClick={addStudent}>Add Student</button>
 </>
  )
}


export default AddStudent;