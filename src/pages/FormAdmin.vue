<template>
  <div class="container-fluid pt-4">
    <div class="row">
      <!-- left -->
      <div class="bd-sidebar col-md-3 col-xl-2 col-12"></div>
      <!-- center -->
      <div class="bd-content col-md-9 col-xl-8 col-12 pb-md-3 pl-md-5">
        <b-spinner variant="info" label="Spinning" v-show="isLoading"></b-spinner>
        <FormComponent
          ref="form"
          v-show="!isLoading"
          v-on:send-training-form="sendForm"
        />
      </div>
      <!-- right -->
      <div class="bd-toc col-xl-2 d-none d-xl-block">
        <div class="side-sticky">
          <ul class="section-nav nav flex-column"></ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import FormComponent from "../components/FormComponent";

export default {
  name: "FormAdmin",
  components: {
    FormComponent
  },
  computed: mapState(["login"]),
  data: function() {
    return {
      isAnswered: true,
      isLoading: true
    };
  },
  mounted: function() {
    if (this.$store.state.login.token) {
      this.isLoading = false;
    }
  },
  beforeRouteUpdate(to, from, next) {
    if (this.$store.state.login.token) {
      next();
      this.isLoading = false;
    } else {
      this.$router.push({ name: "home" });
    }
  },
  methods: {
    sendForm: function(form) {
      this.$toasted.success("Enviando la información...");
      console.log(form);
    }
  },
  watch: {
    // eslint-disable-next-line
    "login.token": function(newValue, oldValue) {
      if (!newValue) {
        // eslint-disable-next-line
        this.$router.push({ name: "home" });
      }
    }
  }
};
</script>

<style>
.bd-sidebar {
  border-right: 1px solid #eee;
}
.bd-toc {
  border-left: 1px solid #eee;
}
</style>