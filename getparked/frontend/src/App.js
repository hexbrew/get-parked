import React from "react";
import { BrowserRouter, Switch } from "react-router-dom";
import RootRouter from "./routers";
import { StoreProvider } from "./store";

import { Header } from "./components/Header";
import { Footer } from "./components/Footer";

import "./App.scss";

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
        <Header />
        <div id="page-body">
          <Switch>
            <RootRouter />
          </Switch>
        </div>
      </BrowserRouter>
      <Header />
      <Footer />
    </StoreProvider>
  );
};

export default App;
