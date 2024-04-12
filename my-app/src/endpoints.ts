import axios from "axios";


export const getBackend = async () => {
    const url = 'http://localhost:5000'
    const res = await axios.get(url)
    return res.data
}
