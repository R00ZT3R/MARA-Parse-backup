import { ChakraProvider, ColorModeScript } from '@chakra-ui/react';
import React, { StrictMode } from 'react';
import ReactDOM from 'react-dom';
import { App } from './App.jsx';

ReactDOM.render(
  <ChakraProvider>
    <ColorModeScript />
    <App />
  </ChakraProvider>,
  document.getElementById('root')
);
