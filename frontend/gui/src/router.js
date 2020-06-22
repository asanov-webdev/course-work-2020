import React from "react";
import { Router, Route } from "react-router-dom";
import { MainPage } from "./components/MainPage/MainPage";
import { Login } from "./components/Login";
import { Register } from "./components/Register";
import { createBrowserHistory } from "history";
import { PrivateRoute } from "./privateRoute";

const history = createBrowserHistory();

export const BaseRouter = () => (
  <Router history={history}>
    <Route path="/login" component={Login} />
    <Route path="/register" component={Register} />
    <PrivateRoute exact path="/" component={MainPage} />
  </Router>
);
