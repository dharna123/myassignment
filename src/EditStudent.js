import { useEffect, useState } from "react"
import axios from "axios"
import { useParams,useNavigate } from "react-router-dom"

function EditStudent()
{
const {id}=useParams()
const navigate=useNavigate()
const [formData,setFormData]=useState({name:"",age:"",course:""})

useEffect(()=>{
    axios.get("http://localhost:5000/students")
    .then(res=>{
       const student= res.data.find(s=>s.id==id)
       setFormData(student)

    }
    )
},[])

const handleChange=(e)=>{

    setFormData({
      ...formData,[e.target.name]:e.target.value
    })
}

const updateStudent=()=>{
    axios.put(`http://localhost:5000/students/${id}`,formData)
    .then(()=>{
        navigate("/")
    })
}
return(


    <>
    <input  name="name" value={formData.name} onChange={handleChange}></input>
 <input  name="age" value={formData.age} onChange={handleChange}></input>
 <input name="course" value={formData.course} onChange={handleChange}></input>
 <button onClick={updateStudent}>Update Student</button>
    
    </>
)
}

export default EditStudent;


