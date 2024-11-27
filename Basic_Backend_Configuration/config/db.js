import mongoose from "mongoose";
import { config } from "./config.js";

const connectDB = async()=>{
    try{
        mongoose.connection.on("connected",()=>{
            console.log(`MongoDB connected successfully`)
        })
        mongoose.connection.on("error", err=>{throw err})

        await mongoose.connect(config.MONODB_URL)

        console.log(`Successfully connected to MongoDB`)
    }catch(err){
        console.log(`Error: ${err}`);
    }
}

export default connectDB;