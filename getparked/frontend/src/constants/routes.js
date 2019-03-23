import prependPath from "../util/prependPath";

const routes = {
  // Root
  root: prependPath(""),

  // Auth
  login: prependPath("login"),

  // Users
  users: {
    root: prependPath("users"),
    profile: prependPath("users/:id"),
    edit: prependPath("users/:id/edit"),
    create: prependPath("users/create")
  }
};

export default routes;
