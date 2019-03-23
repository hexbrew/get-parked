const routes = {
  // Root
  root: "/",

  // Auth
  login: "/login",

  // Users
  users: {
    root: "/users",
    profile: "/users/:id",
    edit: "/users/:id/edit",
    create: "users/create"
  },
};

export default routes;
