import React from "react";
import { useStore } from "../store";

const ThemedButton = (props) => {
  const [{ theme }, dispatch] = useStore();
  return (
    <button
      style={{ backgroundColor: theme.primary }}
      onClick={() =>
        dispatch({
          type: "changeTheme",
          newTheme: { primary: "blue" }
        })
      }
    >
      Make me blue!
    </button>
  );
};

export default ThemedButton;
