<template>
  <div class="container-fluid pt-4">
    <div class="row">
      <!-- left -->
      <div class="bd-sidebar col-md-3 col-xl-2 col-12"></div>
      <!-- center -->
      <div class="bd-content col-md-9 col-xl-8 col-12 pb-md-3 pl-md-5 text-center">
        <div v-if="$store.state.login.token">
          <h1>Template</h1>
          <b-spinner variant="info" label="Spinning" v-if="isLoading" />
          <div v-else>
            <span>Anda a form user </span>
            <span class="text-primary" @click="$router.push({ name: 'form_user', params: { id: 'xxx' }})">acá</span>
            <div v-if="$store.state.login.token">
              <hr/>
              <span>Anda a form admin </span>
              <span class="text-primary" @click="$router.push({ name: 'form_admin', params: { id: 'xxx' }})">acá</span>
            </div>
          </div>
        </div>
        <div v-else>
          <h1>Inicia sesión</h1>
          Debes iniciar sesión para poder usar la plataforma.
        </div>
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

export default {
  name: "Home",
  computed: mapState(["login"]),
  data: function() {
    return {
      isLoading: true
    };
  },
  mounted: function() {
    this.isLoading = false;
  },
  methods: {
    /**showModal: function() {
      const params = {
        title: "Crear paciente",
        patientData: {
          first_name: "",
          last_name: "",
          rut: "",
          email: ""
        },
        // we are passing callback method for our confirm button
        onConfirm: patientData => {
          if (
            patientData.first_name.length > 0 &&
            patientData.last_name.length > 0
          ) {
            this.createPatient(patientData);
            return true;
          } else {
            this.$toasted.error(
              "Debes agregar el nombre y apellido del paciente!"
            );
            return false;
          }
        },
        confirmText: "Crear"
      };
      this.$patientModal.show(params);
    }**/
  },
  watch: {
    // eslint-disable-next-line
    "login.token": function(newValue, oldValue) {
      if (newValue) {
        // DO STUFF
      } else {
        // DO STUFF
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