import React, {useEffect, useState} from 'react';
import './App.css';
import {TextField} from "@mui/material";
import {getBackend} from "./endpoints";

function App() {
    const [textInput, setTextInput] = useState<string>('')
    const [data, setData] = useState<string>('')

    useEffect(()=>{
        getBackend()
            .then(res=>setData(res))
            .catch(err=>console.error(err))
    },[])

  return (
    <div className="App">
      <header className="App-header">
        <div className='text-3xl mb-10'>Hello, enter your name:</div>
          <TextField
              className='bg-white'
              variant="outlined"
              value={textInput}
              label={'Enter name'}
              onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                  setTextInput(event.target.value);
              }}
          />
          {textInput && (
              <div className='mt-10'>Hello, <span className='text-orange-500'>{textInput}</span>!</div>
          )}
          <div>Data from database:</div>
          <div>{data}</div>
      </header>
    </div>
  );
}

export default App;
