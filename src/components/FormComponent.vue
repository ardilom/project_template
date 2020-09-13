<template>
  <div class="w-100" style="min-height:38px;text-align:left;">
    <h2>Hola {{form.firstName}} {{form.lastName}}!</h2>
    <p>Por favor contesta este formulario.</p>
    <b-form>
      <b-form-group label="Fecha de nacimiento" label-for="input-birth">
        <b-form-input v-model="form.birth" type="date" min="0" id="input-birth" />
      </b-form-group>
      <b-form-group label="Correo" label-for="input-email">
        <b-form-input
          v-model="form.email"
          type="email"
          placeholder="correo@mail.cl"
          id="input-email"
        />
      </b-form-group>
      <b-form-group label="Teléfono" label-for="input-phone">
        <b-form-input v-model="form.phone" placeholder="912345678" id="input-phone" />
      </b-form-group>
      <b-form-group label="Sexo" label-for="input-sex">
        <b-form-select v-model="form.sex" :options="options.optionsSex" id="input-sex" />
      </b-form-group>
      <b-form-group
        label="Seleccione el(los) grupo(s) de ejercicios más similar(es) a su rutina habitual de entrenamiento"
        label-for="input-image"
      >
        <b-form-checkbox-group id="input-image" v-model="form.image">
          <b-form-checkbox value="1" class="option-image">
            <img src="../assets/img/logo-vue.png" alt="option1" />
          </b-form-checkbox>
          <b-form-checkbox value="2" class="option-image">
            <img src="../assets/img/logo-vue.png" alt="option2" />
          </b-form-checkbox>
          <b-form-checkbox value="3" class="option-image">
            <img src="../assets/img/logo-vue.png" alt="option3" />
          </b-form-checkbox>
          <b-form-checkbox value="4" class="option-image">
            <img src="../assets/img/logo-vue.png" alt="option4" />
          </b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>
      <b-button
        type="button"
        @click="sendForm()"
        class="my-4"
        variant="primary"
      >Responder cuestionario</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: mapState(["login"]),
  data: function() {
    return {
      form: {
        firstName: "Usuario",
        lastName: "Falso",
        rut: "",
        birth: "",
        email: "",
        phone: "",
        sex: null,
        image: []
      },
      options: {
        optionsSex: [
          { value: 1, text: "Mascúlino" },
          { value: 2, text: "Femenino" }
        ]
      }
    };
  },
  methods: {
    sendForm: function() {
      this.$emit("send-training-form", this.form);
    },
    loadForm: function(data) {
      this.form = data;
    }
  }
};
</script>

<style>
.option-image {
  display: inline-block;
  width: 50%;
  padding-bottom: 0.25rem;
  padding-top: 0.25rem;
  margin: 0;
}
</style>