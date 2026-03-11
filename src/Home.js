import {useEffect, useState } from "react"
import { Link,useNavigate } from "react-router-dom"
import axios from "axios"

function Home()
{
   const navigate=useNavigate()
    const [students,setStudents]=useState([])

    const fetchStudents=()=>{
        axios.get("http://localhost:5000/students")
        .then(res=>{
            setStudents(res.data)
        }
        )
    }

  useEffect(()=>{
    fetchStudents()
  },[])

  const deleteStudent=(id)=>{
    axios.delete(`http://localhost:5000/students/${id}`)
    .then(()=>{
        fetchStudents()
    })
  }

  return(

    <>
    <table border="2">
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Course</th>
            <th colSpan={2}>Action</th>
            
        </tr>
       
            {students.map(s=>(
                <>
                <tr>
                <td>{s.name}</td>
                <td>{s.age}</td>
                <td>{s.course}</td>
                <td><button onClick={()=>navigate(`/edit/${s.id}`)}>Edit</button></td>
                <td><button onClick={()=>deleteStudent(s.id)}>Delete</button></td>
                </tr>
                </>
            ))}
       


    </table>
    <Link to="/add">
    <button>Add Student</button>
    </Link>
    
    </>



  )

}

export default Home;