/**
 * The store uses the React Context API to provide global state management.
 * See App component for setup example.
 * See ThemedButton component for usage example.
 */

import React from "react";
import { createContext, useContext, useReducer } from "react";
export const StoreContext = createContext();
export const StoreProvider = ({ reducer, initialState, children }) => (
  <StoreContext.Provider value={useReducer(reducer, initialState)}>
    {children}
  </StoreContext.Provider>
);
export const useStore = () => useContext(StoreContext);
