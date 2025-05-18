const data = require("./database");
const express = require("express");
const app = express();
let port = 3000;
app.get("/",async (req,res)=>{
    const name = await data.find();
    console.log(name); 
});
app.listen(port,()=>{
    console.log("server is running");
});