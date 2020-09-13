<template>
  <div id="app">
    <component :is="layout">
      <router-view />
    </component>
    <delete-modal />
  </div>
</template>


<script>
const defaultLayout = "default"
import { mapState } from "vuex"
import notificationService from "./services/notificationService"

export default {
  computed: {
    layout() {
      return this.$route.meta.layout || defaultLayout
    },
    ...mapState(["login"])
  },
  created() {
    const vueScope = this;
    if (this.$store.state.login.token) {
      this.getMyNotifications()
      //this.$connect()
    }
    this.$options.sockets.onmessage = data =>
      vueScope.$toasted.success(JSON.parse(data.data).message)
  },
  methods: {
    getMyNotifications: function() {
      notificationService.get_my_notifications().then(
        data => {
          this.$store.commit("login/setNotifications", data)
        },
        error => {
          console.error(error);
        }
      );
    }
  },
  watch: {
    // eslint-disable-next-line
    "login.token": function(newValue, oldValue) {
      if (newValue) {
        this.$toasted.success("Sesión iniciada exitosamente.");
        //this.$connect("ws://127.0.0.1:8000/socket/" + newValue)
        this.getMyNotifications();
      } else {
        this.$toasted.success("Sesión cerrada exitosamente.")
        this.$disconnect()
        this.$store.commit("login/setNotifications", { notifications: [] })
      }
    }
  }
};
</script>

<style lang="scss">
@import "./assets/scss/template";
</style>
