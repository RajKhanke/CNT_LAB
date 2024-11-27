import Books from "../models/Book.js";
import extractBookInfo from "../utility/bookUtility/extractBookInfo.js";

const bookController = {
createBook: async(req,res,next) =>{
    try{
        const {title,description,genre} = req.body
        const files = req.files;
        console.log(files);
        console.log(title,description,genre);

        // Extract the coverImage Info

        const coverImageInfo = extractBookInfo(files, "coverImage","book-cover");
        console.log("CoverImage: ",coverImageInfo);
        
        const newBook = new Books({title,description,genre})
        await newBook.save()

        res.json({
            message: "Book Created Successfully"
        })

    }catch(err){
        console.log("Error in create Book",err)
    }
},

listBooks: async(req,res,next)=>{

    const books = await Books.find() // Assuming that you have Books database in your MongoDB
    res.json({books})
}
    }

export default bookController
