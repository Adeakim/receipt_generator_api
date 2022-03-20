import React, { useState } from "react";
import { useHistory } from "react-router";


const Create = () => {
    const[name,setName]=useState('')
    const[address,setAddress]=useState('')
    const[mobileNumber,setmobileNumber]=useState('')
    const[totalAmountPayable,setTotalAmountPayable]=useState('mario')
    const[ispending,setIsPending]=useState(false)
    const history=useHistory()

    const handleSubmit=(e)=>{
        e.preventDefault()
        const blog ={name,address,mobileNumber,totalAmountPayable}
        setIsPending(true)
        const token = localStorage.getItem('token')
        fetch('https://receipt-generator-api.herokuapp.com/api/v1/generate-receipt/',{
            method:"POST",
            headers:{"content-type":"application/json"},
            Authorization: token,
            body:JSON.stringify(blog)
        }).then(()=>{
            // console.log("registerd")
            setIsPending(false)
            history.push("/receipt")
        })
    }

    return (  
        <div className="create">

            <form onSubmit={handleSubmit}>
                    <label>Name</label>
                    <input type="text"t
                        required
                        value={name}
                        onChange={(e)=>setName(e.target.value)}
                    />
                    <label >Address</label>
                    <input type="text"t
                        required
                        value={address}
                        onChange={(e)=>setAddress(e.target.value)}
                    />
                    <label>Mobile Number</label>
                    <input type="text"t
                        required
                        value={mobileNumber}
                        onChange={(e)=>setmobileNumber(e.target.value)}
                    />
                     <label>Total Amount Payable</label>
                    <input type="text"
                        required
                        value={totalAmountPayable}
                        onChange={(e)=>setTotalAmountPayable(e.target.value)}
                    />
                    {!ispending && <button>Generate Receipt</button>}
                    {ispending && <button disabled>Generating Receipt</button>}
                </form>
        </div>
        
    );
}
 
export default Create;
