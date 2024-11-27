import {config as con} from "dotenv"
con()

const _config = {
    PORT: process.env.PORT,
    MONODB_URL: process.env.MONODB_URL,
    
}
export const config = Object.freeze(_config)