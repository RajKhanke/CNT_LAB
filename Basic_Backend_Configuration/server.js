import app from "./app.js";
import connectDB from "./config/db.js";

const main  = async() =>{
    try{

        const PORT = process.env.PORT || 3000;
        app.listen(PORT,
             () => console.log(`Server running on port ${PORT}.`)
        )

        await connectDB()
    }catch(err){
        console.error(err);
    }
}
main()