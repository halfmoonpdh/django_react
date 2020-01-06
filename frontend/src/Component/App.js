import React from "react";
import styled, { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  body{
    padding: 0;
    margin: 0;
  }
`;

const Container = styled.div`
  height: 100vh;
  width: 100%;
  background-color: #bdc3c7;
`;

class App extends React.Component {
  render() {
    return (
      <Container>
        <GlobalStyle />
      </Container>
    );
  }
}

export default App;
