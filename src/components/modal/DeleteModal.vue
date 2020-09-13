<template>
  <div>
    <b-modal id="delete-modal" :title="title">
      <p class="my-4">{{text}}</p>
      <template v-slot:modal-footer>
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-button size="sm" variant="danger" @click="confirm()">
          Eliminar
        </b-button>
        <b-button size="sm" variant="outline-info" @click="hide()">
          Cancelar
        </b-button>
      </template>
    </b-modal>
  </div>
</template>


<script>
// we must import our Modal plugin instance
// because it contains reference to our Eventbus
import DeleteModal from '../../utils/delete-modal.js';

export default {
  data() {
    return {
      title: "",
      text: "",
      onConfirm: {},
    };
  },
  methods: {
    hide() {
      this.$bvModal.hide("delete-modal")
    },
    confirm() {
      // we must check if this.onConfirm is function
      if(typeof this.onConfirm === 'function') {
        // run passed function and then close the modal
        this.onConfirm()
        this.$bvModal.hide("delete-modal")
      }
    },
    show(params) {
      // setting title and text
      this.title = params.title
      this.text = params.text
      // setting callback function
      this.onConfirm = params.onConfirm
      this.$bvModal.show("delete-modal")
    }
  },
  beforeMount() {
    // here we need to listen for emited events
    // we declared those events inside our plugin
    DeleteModal.EventBus.$on('show', (params) => {
      this.show(params)
    })
  }
};
</script>