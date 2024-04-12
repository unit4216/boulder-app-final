import axios from "axios";

const baseUrl = 'http://localhost:5000'

export const getAirQualityIndex = async (latitude: number, longitude: number) => {
    const url = `${baseUrl}/aqi?latitude=${latitude}&longitude=${longitude}`
    const res = await axios.get(url)
    return res.data
}

export const getPastPredictions = async () => {
    const url = `${baseUrl}/get-past-predictions`
    const res = await axios.get(url)
    return res.data
}
