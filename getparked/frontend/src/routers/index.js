import React from "react";
import { Route } from "react-router-dom";
import routes from "../constants/routes";

import Aux from "../components/Aux";

import Dashboard from '../screens/Dashboard'
import UserRouter from '../routers/UserRouter'

const Routes = props => {
  return (
    <Aux>
      {/* Root */}
      <Route exact path={routes.root} component={Dashboard} />

      {/* Modules */}
      <Route path={routes.users.root} component={UserRouter} />
    </Aux>
  );
};

export default Routes;
