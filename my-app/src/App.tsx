import React, {useEffect, useState} from 'react';
import './App.css';
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
          <div>The air quality index at TD Garden Stadium next hour is predicted to be:</div>
          <div>{data}</div>
      </header>
    </div>
  );
}

export default App;
