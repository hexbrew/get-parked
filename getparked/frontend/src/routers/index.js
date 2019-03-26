import React from "react";
import { Route } from "react-router-dom";
import routes from "../constants/routes";

import Wrapper from "../components/Wrapper";

import Dashboard from '../screens/Dashboard'
import UserRouter from '../routers/UserRouter'

const Routes = props => {
  return (
    <Wrapper>
      {/* Root */}
      <Route exact path={routes.root} component={Dashboard} />

      {/* Modules */}
      <Route path={routes.users.root} component={UserRouter} />
    </Wrapper>
  );
};

export default Routes;
