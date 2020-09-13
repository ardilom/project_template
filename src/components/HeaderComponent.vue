<template>
  <b-navbar toggleable="lg" type="dark" variant="primary" id="template-navbar">
    <b-navbar-brand href="#" @click="$router.push({ name: 'home'}).catch(err => {})">Template</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse" />

    <b-collapse id="nav-collapse" is-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown v-if="$store.state.login.token" right no-caret>
          <!-- Using 'button-content' slot -->
          <template slot="button-content">
            <b-button variant="outline-primary">
              &#128276;
              <b-badge variant="warning">{{$store.state.login.notifications.length}}</b-badge>
            </b-button>
          </template>
          <b-dropdown-item
            href="#"
            v-for="(notification, index) in $store.state.login.notifications"
            :key="'b-dropdown-item'+index"
          >
            <span v-on:click.stop v-html="notification.message" />
          </b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item-dropdown ref="loginDropdown" v-if="!$store.state.login.token" right>
          <!-- Using 'button-content' slot -->
          <template slot="button-content">
            <em>Iniciar sesión</em>
          </template>
          <LoginComponent @hide-login-dropdown="hideLoginDropdown()"></LoginComponent>
        </b-nav-item-dropdown>
        <b-nav-item-dropdown v-else right>
          <!-- Using 'button-content' slot -->
          <template slot="button-content">
            <b-img
              :src="$store.state.login.thumbnail"
              width="35"
              height="35"
              rounded="circle"
              alt="Circle image"
              class="mr-1"
            ></b-img>
            <em>{{$store.state.login.first_name}} {{$store.state.login.last_name}}</em>
          </template>
          <b-dropdown-item href="#" @click="$store.commit('login/setUserEmpty')">
            Cerrar sesión
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import LoginComponent from "../components/LoginComponent";
export default {
  components: {
    LoginComponent
  },
  methods: {
    hideLoginDropdown: function() {
      this.$refs.loginDropdown.hide();
    }
  }
};
</script>

<style lang="scss">
</style>