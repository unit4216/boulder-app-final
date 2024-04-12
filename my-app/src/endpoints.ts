import axios from "axios";


export const getBackend = async () => {
    const url = 'http://localhost:5000/data'
    const res = await axios.get(url)
    return res.data
}
