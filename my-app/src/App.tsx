import React, {useState} from 'react';
import './App.css';
import {TextField} from "@mui/material";

function App() {
    const [textInput, setTextInput] = useState<string>('')

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
      </header>
    </div>
  );
}

export default App;
