import path from "node:path";
import { fileURLToPath } from "url";

// Define __dirname manually for ES Module compatibility
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const extractBookInfo = (files, fieldname, folder) => {
    const fileName = files[fieldname][0].filename;
    const format = files[fieldname][0].mimetype.split("/").at(-1);
    const filePath = path.resolve(__dirname, "../../public/data/uploads", fileName);

    return { fileName, format, folder };
};

export default extractBookInfo;
