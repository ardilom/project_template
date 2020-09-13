import App from "./App";
import axios from "axios";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import Default from "./layouts/Default";
import DeleteModal from "./utils/delete-modal";
//import LogRocket from "logrocket";
import router from "@/router";
import store from "./store/index";
import Toasted from "vue-toasted";
import Vue from "vue";
import VueAxios from "vue-axios";
import VueNativeSock from "vue-native-websocket";

// libs
//LogRocket.init("xxxx");
Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.use(Toasted, {
  position: "bottom-left",
  duration: 5000,
  theme: "outline",
  action: {
    text: "x",
    onClick: (e, toastObject) => {
      toastObject.goAway(0);
    }
  }
});

// custom plugins
Vue.use(DeleteModal);

// layouts
Vue.component("default", Default);

// sockets
Vue.use(
  VueNativeSock,
  "ws://127.0.0.1:8000/socket/" + localStorage.getItem("token"),
  {
    connectManually: true,
    store: store,
    format: "json"
  }
);

new Vue({
  store: store,
  router,
  render: h => h(App)
}).$mount("#app");
