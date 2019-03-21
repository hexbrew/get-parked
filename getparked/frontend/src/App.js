import React from "react";
import { StoreProvider } from "./store";
import ThemedButton from "./components/ThemedButton";

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
      <ThemedButton />
    </StoreProvider>
  );
};

export default App;
