import { Router } from "express";
import bookController from "../controllers/bookController.js";
import multer from "multer";
const upload = multer({ dest: 'uploads/' })

const router = Router()

router.post("/",
    upload.fields([{ name: 'coverImage', maxCount: 1 }, { name: 'file', maxCount: 1 }]),
    bookController.createBook)

router.get("/", bookController.listBooks)

export default router;
