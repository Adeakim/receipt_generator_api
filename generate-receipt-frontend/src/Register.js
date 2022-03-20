import React, { useState } from "react";
import { useHistory } from "react-router";


const Create = () => {
    const[name,setName]=useState('')
    const[email,setEmail]=useState('')
    const[address,setAddress]=useState('')
    const[mobileNumber,setmobileNumber]=useState('')
    const[password,setPassword]=useState('')
    const[confirmPassword,setconfirmPassword]=useState('')  
    const[ispending,setIsPending]=useState(false)
    // const [message, setMessage] = useState("");
    const history=useHistory()

    const handleSubmit=(e)=>{
        e.preventDefault()
        const data ={name,email,address,mobileNumber,password,confirmPassword}
        setIsPending(true)

        fetch('http://127.0.0.1:8000/api/v1/auth/register/',{
            method:"POST",
            headers:{"content-type":"application/json"},
            body:JSON.stringify(data)
        })
        .then(()=>{
            console.log(data)
            setIsPending(false)
            // history.push("/login")
        })
    }

    return (  
        <div className="create">

            <form onSubmit={handleSubmit}>
                    <label>Name</label>
                    <input type="text"t
                        required
                        value={name}
                        name= "name"
                        onChange={(e)=>setName(e.target.value)}
                    />
                    <label >Address</label>
                    <input type="text"t
                        required
                        value={address}
                        name="address"
                        onChange={(e)=>setAddress(e.target.value)}
                    />
                    <label >Email</label>
                    <input type="text"t
                        required
                        value={email}
                        name="email"
                        onChange={(e)=>setEmail(e.target.value)}
                    />
                    <label>Mobile Number</label>
                    <input type="text"t
                        required
                        value={mobileNumber}
                        name="mobileNumber"
                        onChange={(e)=>setmobileNumber(e.target.value)}
                    />
                     <label>Password</label>
                    <input type="text"t
                        required
                        value={password}
                        name="password"
                        onChange={(e)=>setPassword(e.target.value)}
                    />
                     <label>Confirm Password</label>
                    <input type="text"t
                        required
                        name="confirmPassword"
                        value={confirmPassword}
                        onChange={(e)=>setconfirmPassword(e.target.value)}
                    />
                    {!ispending && <button type="submit">Submit</button>}
                    {ispending && <button disabled>submitting ...</button>}
                </form>
        </div>
        
    );
}
 
export default Create;
