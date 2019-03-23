import React from "react";
import style from "./App.less"
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
      <h1 class={style.waste}>Test H1 Tag</h1>
    </StoreProvider>
  );
};

export default App;
