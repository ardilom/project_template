import auth from "../services/authService";
import store from "../store/";

export const authMixin = {
  methods: {
    authenticate_password: function(payload) {
      var vue_context = this;
      auth
        .authenticate_password(payload)
        .then(response => {
          if (response.token) {
            store.commit("login/setUser", response);
          } else {
            vue_context.$toasted.error(
              "Correo o contraseña incorrectas"
            );
            store.commit("login/setUserEmpty");
          }
        })
        // eslint-disable-next-line
        .catch(error => {
          vue_context.$toasted.error(
            "Ha ocurrido un error en el servidor, intenta más tarde."
          );
          store.commit("login/setUserEmpty");
        });
    },
    register_user: function(payload) {
      var vue_context = this;
      auth
        .register(payload)
        .then(response => {
          if (response && response.message) {
            vue_context.$toasted.success(response.message);
          }
        })
        .catch(error => {
          if (
            error.response &&
            error.response.data &&
            error.response.data.message
          ) {
            vue_context.$toasted.error(
              error.response.data.message
            );
          } else {
            vue_context.$toasted.error(
              "Ha ocurrido un error en el servidor, intenta más tarde."
            );
          }
        });
    }
  }
};
