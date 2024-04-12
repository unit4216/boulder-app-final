import React, {useEffect, useState} from 'react';
import './App.css';
import {getAirQualityIndex, getPastPredictions} from "./endpoints";
import {Box, FormControl, InputLabel, MenuItem, Select} from "@mui/material";
import {DataGrid, GridColDef} from "@mui/x-data-grid";

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

interface PredictionRow {
    aqi: string,
    generated_at: string,
    latitude: string,
    longitude: string,
    prediction_hour: string
}

const columns: GridColDef[] = [
    {
        field: 'aqi',
        headerName: 'AQI',
        flex: 1
    },
    {
        field: 'generated_at',
        headerName: 'Generated At',
        flex: 1
    },
    {
        field: 'latitude',
        headerName: 'Latitude',
        flex: 1
    },
    {
        field: 'longitude',
        headerName: 'Longitude',
        flex: 1
    },
    {
        field: 'prediction_hour',
        headerName: 'Prediction Hour',
        flex: 1
    }
]

function App() {
    const [airQualityIndex, setAirQualityIndex] = useState<string>('')
    const [selectedCity, setSelectedCity] = useState<City>(cityCoordinates[0])
    const [pastPredictions, setPastPredictions] = useState<PredictionRow[]>([])

    useEffect(()=> {
        getAirQualityIndex(selectedCity.latitude, selectedCity.longitude)
            .then(res=>setAirQualityIndex(res))
            .catch(err=>console.error(err))
    },[selectedCity])

    useEffect(()=>{
        getPastPredictions()
            .then(res=>setPastPredictions(res))
            .catch(err=>console.error(err))
    },[selectedCity])

    const relevantBound = airQualityIndexBounds
        .find(bound => {
            const [lowerBound, upperBound] = bound.range
            const numericalQualityIndex = parseFloat(airQualityIndex)
            return numericalQualityIndex >= lowerBound && numericalQualityIndex <= upperBound
        })

    const formattedAqi = parseFloat(airQualityIndex).toFixed(2)

  return (
    <div className="App">
      <header className="App-header">
          <FormControl className='w-64'>
              <InputLabel>Select City</InputLabel>
              <Select
                  value={selectedCity}
                  label="Select City"
                  onChange={(e) => setSelectedCity(e.target.value as City)}
              >
                  {cityCoordinates.map(city => {
                      // @ts-ignore
                      return <MenuItem value={city}>{city.city}</MenuItem>
                  })}
              </Select>
          </FormControl>
          <div className='mt-10'>
              The air quality index in &nbsp;
              <span className='font-bold'>{selectedCity.city}</span>
              &nbsp; next hour is predicted to be &nbsp;
              <span className='font-bold'>{formattedAqi}</span>
          </div>
          <div>
              This is considered &nbsp;
              <span className='font-bold'>{relevantBound?.label}</span>
              &nbsp; on the US Air Quality Index
          </div>
          <div className='mt-10 mb-2'>Previous predictions:</div>
          <Box sx={{ height: 400, width: '50%' }}>
              <DataGrid
                  rows={pastPredictions}
                  columns={columns}
                  getRowId={() => Math.random()}
              />
          </Box>
      </header>
    </div>
  );
}

export default App;
