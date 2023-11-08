import React from 'react';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import { Main, Result } from '../pages';

export default function MainRoute() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="" element={<Main />} />
        <Route path="Result" element={<Result />} />
      </Routes>
    </BrowserRouter>
  );
}