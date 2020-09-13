<template>
  <div>
    <b-modal :id="id" :title="title">
      {{text}}
      <template v-slot:modal-footer>
        <b-button size="sm" variant="info" @click="confirm()">{{confirmText}}</b-button>
        <b-button size="sm" variant="outline-info" @click="hide()">{{cancelText}}</b-button>
      </template>
    </b-modal>
  </div>
</template>


<script>
export default {
  data() {
    return {
      modalData: {
        id: "",
        title: "",
        onConfirm: {},
        confirmText: "",
        cancelText: ""
      }
    };
  },
  methods: {
    hide() {
      this.$bvModal.hide(this.modalData.id);
    },
    confirm() {
      // we must check if this.onConfirm is function
      if (typeof this.modalData.onConfirm === "function") {
        // run passed function and then close the modal
        let close = this.modalData.onConfirm();
        if (close) {
          this.$bvModal.hide(this.modalData.id);
        }
      }
    },
    show(params) {
      // setting title and text
      this.modalData = params;
      this.$bvModal.show(this.modalData.id);
    }
  }
};
</script>