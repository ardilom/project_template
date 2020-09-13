<template>
  <div class="container-fluid pt-4">
    <div class="row">
      <!-- left -->
      <div class="bd-sidebar col-md-3 col-xl-2 col-12"></div>
      <!-- center -->
      <div class="bd-content col-md-9 col-xl-8 col-12 pb-md-3 pl-md-5">
        <b-spinner variant="info" label="Spinning" v-if="isLoading"></b-spinner>
        <p v-else-if="recentlyAnswered">Gracias por contestar la encuesta!</p>
        <p v-else-if="isAnswered">Lo sentimos pero esta encuesta ya ha sido respondida!</p>
        <FormComponent
          v-show="!isAnswered && !isLoading && !recentlyAnswered"
          ref="form"
          v-on:send-training-form="sendForm"
        ></FormComponent>
      </div>
      <!-- right -->
      <div class="bd-toc col-xl-2 d-none d-xl-block">
        <div class="side-sticky">
          <ul class="section-nav nav flex-column">
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FormComponent from "../components/FormComponent";
import { mapState } from "vuex";

export default {
  name: 'FormUser',
  components: {
    FormComponent
  },
  computed: mapState(["login"]),
  data: function() {
    return {
      isLoading: true,
      isAnswered: false,
      recentlyAnswered: false
    };
  },
  mounted: function() {
    this.isLoading = false;
  },
  beforeRouteUpdate(to, from, next) {
    next();
    // DO SAME AS MOUNTED
    this.isLoading = false;
  },
  methods: {
    sendForm: function(form) {
      this.$toasted.success("Enviando la información...");
      console.log(form);
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