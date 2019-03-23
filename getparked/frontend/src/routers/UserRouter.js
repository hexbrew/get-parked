import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";

/* Custom routing */
import routes from "../constants/routes";

/* Module */
import ProfileEdit from "../screens/ProfileEdit";

class UserRouter extends Component {
  render() {
    return (
      <Switch>
        <Route
          exact
          path={routes.users.edit}
          component={ProfileEdit}
        />
      </Switch>
    );
  }
}

export default UserRouter;
