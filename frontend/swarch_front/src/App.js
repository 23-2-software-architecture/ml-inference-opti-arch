import React from 'react';
import { Reset } from 'styled-reset'
import MainRoute from './route/MainRoute';

function App() {
  return (
    <React.Fragment>
      <Reset />
      <MainRoute/>
    </React.Fragment>
  );
}

export default App;
