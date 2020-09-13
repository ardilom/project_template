import Home from "./pages/Home";
import FormAdmin from "./pages/FormAdmin";
import FormUser from "./pages/FormUser";
import Router from "vue-router";
import store from "./store/";
import Vue from "vue";

Vue.use(Router);

const isAuthenticated = (to, from, next) => {
  if (store.state.login.token) {
    next();
  } else {
    next("/");
  }
};

export default new Router({
  routes: [
    { path: "", component: Home, name: "home" },
    { path: "/form/:id", component: FormUser, name: "form_user" },
    {
      path: "/form/:id/admin",
      component: FormAdmin,
      name: "form_admin",
      beforeEnter: isAuthenticated
    }
  ]
});
