import React from "react";
import styled, { createGlobalStyle } from "styled-components";
import axios from "axios";

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

const Card = styled.div``;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null
    };
  }
  componentDidMount = async () => {
    let data = null;
    try {
      ({ data } = await axios.get(
        "http://127.0.0.1:8000/demo_user/?format=json",
        {
          header: {
            "Access-Control-Allow-Origin": "*"
          }
        }
      ));
    } catch (error) {
    } finally {
      this.setState({ data });
    }
  };
  render() {
    const { data, loaded, placeholder } = this.state;
    return (
      <Container>
        <GlobalStyle />
        {data &&
          data.map((demo_user, index) => (
            <Card key={index}>{demo_user.name}</Card>
          ))}
      </Container>
    );
  }
}

export default App;
