import React, {useEffect, useState} from 'react';
import './App.css';
import {getAirQualityIndex} from "./endpoints";
import {FormControl, InputLabel, MenuItem, Select} from "@mui/material";

interface City {
    city: string,
    latitude: number,
    longitude: number
}

const cityCoordinates: City[] = [
    {city: "Boston", latitude: 42.3601, longitude: -71.0589},
    {city: "Houston", latitude: 29.7604, longitude: -95.3698},
    {city: "Los Angeles", latitude: 34.0549, longitude: -118.2426},
    {city: "New York City", latitude: 40.7127, longitude: -74.0059},
    {city: "N'Djamena, Chad", latitude: 12.1191, longitude: 15.0503},
]

interface AqiBound {
    range: [number, number],
    label: string
}

const airQualityIndexBounds: AqiBound[] = [
    {range: [0, 50], label: 'Good'},
    {range: [51, 100], label: 'Moderate'},
    {range: [101, 150], label: 'Unhealthy for Sensitive Groups'},
    {range: [151, 200], label: 'Unhealthy'},
    {range: [201, 300], label: 'Very Unhealthy'},
    {range: [301, 500], label: 'Hazardous'}
]

function App() {
    const [airQualityIndex, setAirQualityIndex] = useState<string>('')
    const [selectedCity, setSelectedCity] = useState<City>(cityCoordinates[0])

    useEffect(()=> {
        getAirQualityIndex(selectedCity.latitude, selectedCity.longitude)
            .then(res=>setAirQualityIndex(res))
            .catch(err=>console.error(err))
    },[selectedCity])

    const relevantBound = airQualityIndexBounds
        .find(bound => {
            const [lowerBound, upperBound] = bound.range
            const numericalQualityIndex = parseFloat(airQualityIndex)
            return numericalQualityIndex >= lowerBound && numericalQualityIndex <= upperBound
        })

  return (
    <div className="App">
      <header className="App-header">
          <FormControl className='w-64'>
              <InputLabel>Select City</InputLabel>
              <Select
                  value={selectedCity}
                  label="Select City"
                  onChange={(e) => setSelectedCity(e.target.value)}
              >
                  {cityCoordinates.map(city => {
                      return <MenuItem value={city}>{city.city}</MenuItem>
                  })}
              </Select>
          </FormControl>
          <div>The air quality index in {selectedCity.city} next hour is predicted to be:</div>
          <div>{airQualityIndex}</div>
          <div>This is: {relevantBound?.label}</div>
      </header>
    </div>
  );
}

export default App;
