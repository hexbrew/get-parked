import React from "react";
import "./App.scss";
import { StoreProvider } from "./store";
import { Header } from "./components/Header"
import { Footer } from "./components/Footer"

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
      <Header />
      {/* TODO: Route view for body */}
      <Footer />
    </StoreProvider>
  );
};

export default App;
