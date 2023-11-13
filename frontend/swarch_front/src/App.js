import React from 'react';
import { Reset } from 'styled-reset';
import {
  RecoilRoot,
} from 'recoil';
import { Main } from './pages';

function App() {
  return (
    <React.Fragment>
      <RecoilRoot>
        <Reset />
        <Main />
      </RecoilRoot>
    </React.Fragment>
  );
}

export default App;
