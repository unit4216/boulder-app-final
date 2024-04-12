import axios from "axios";


export const getAirQualityIndex = async (latitude: number, longitude: number) => {
    const url = `http://localhost:5000/aqi?latitude=${latitude}&longitude=${longitude}`
    const res = await axios.get(url)
    return res.data
}
