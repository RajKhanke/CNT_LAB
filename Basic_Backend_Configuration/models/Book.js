import { model, Schema } from "mongoose";

const bookSchema = new Schema({
    title:{
        type: String,
        required: true
    },
    description:{
        type: String,
        required:true
    },
    coverImg:{
        type:String,
        // required: true
    },
    genre:{
        type: String,
        required: true
    },
    file:{
        type:String,
        // required: true
    }
},{timestamps: true});

const Books = new model("Books",bookSchema);

export default Books;