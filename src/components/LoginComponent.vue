<template>
  <div>
    <b-dropdown-form ref="dropdown" style="min-width: 278px;">
      <b-form>
        <b-form-group label="Email" label-for="dropdown-form-email">
          <b-form-input
            size="sm"
            placeholder="email@example.com"
            v-model="email"
            @keyup.enter="authenticate_password({email: email, password: password})"
          />
        </b-form-group>
        <b-form-group label="Password" label-for="dropdown-form-password">
          <b-form-input
            type="password"
            size="sm"
            placeholder="Password"
            v-model="password"
            @keyup.enter="authenticate_password({email: email, password: password})"
          />
        </b-form-group>
        <br />
        <b-button
          size="sm"
          variant="primary"
          class="my-2 my-sm-0 mr-1"
          @click="authenticate_password({email: email, password: password})"
          v-if="!$store.state.login.token"
          right
        >Iniciar Sesión</b-button>
      </b-form>
    </b-dropdown-form>
  </div>
</template>

<script>
import { authMixin } from "../mixins/authMixin";
export default {
  mixins: [authMixin],
  data: function() {
    return {
      email: "",
      password: "",
    };
  }
};
</script>

<style>
</style>