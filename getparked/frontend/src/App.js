import React from "react";
import "./App.scss";
import { StoreProvider } from "./store";
import { Header } from "./components/Header";

import { BrowserRouter, Switch } from "react-router-dom";
import RootRouter from "./routers";

const App = () => {
  const initialState = { theme: { primary: "green" } };

  const reducer = (state, action) => {
    switch (action.type) {
      case "changeTheme":
        return {
          ...state,
          theme: action.newTheme
        };

      default:
        return state;
    }
  };

  return (
    <StoreProvider initialState={initialState} reducer={reducer}>
      <BrowserRouter>
        {/* <Aux> */}
        <Header />
        <Switch>
          <RootRouter />
        </Switch>
        {/* </Aux> */}
      </BrowserRouter>
    </StoreProvider>
  );
};

export default App;
