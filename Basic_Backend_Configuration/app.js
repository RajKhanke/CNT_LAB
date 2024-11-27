import express from "express"; 
import bookRoute from "./routes/bookRoute.js";
import globalErrorHandler from "./middlewares/globalErrorHandler.js";

const app = express()

app.use("/api/book",bookRoute);

app.use(express.json())

app.use(globalErrorHandler)

export default app;