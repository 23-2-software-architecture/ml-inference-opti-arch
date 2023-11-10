import React from 'react';
import { Reset } from 'styled-reset'
import MainRoute from './route/MainRoute';
import {
  RecoilRoot,
} from 'recoil';

function App() {
  return (
    <React.Fragment>
      <RecoilRoot>
        <Reset />
        <MainRoute/>
      </RecoilRoot>
    </React.Fragment>
  );
}

export default App;
