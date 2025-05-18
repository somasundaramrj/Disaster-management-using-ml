const mongoose = require("mongoose");

main().then(()=>{
    console.log("connected succesfully");
}).catch((err)=>{
    console.log("error occured while connceting the database");
})
async function main(){
    await mongoose.connect("mongodb://127.0.0.1:27017/Disastermanagment");
}
const Citizen = new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true
    },
    password :{
        type:String,
        required:true
    },
    phone :{
        type:String,
        required:true
    },
    location:{
        type:String,
        required:true
    },
    emergency : {
        type:String,
        required :true
    }
});

const User = mongoose.model("User",Citizen);
module.exports=User;