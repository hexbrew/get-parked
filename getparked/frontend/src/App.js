import React from "react";
import "./App.scss";
import { StoreProvider } from "./store";
import ThemedButton from "./components/ThemedButton";
import { NavigationBar } from "./components/nav/NavigationBar";

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
      <NavigationBar />
      <ThemedButton />
    </StoreProvider>
  );
};

export default App;
