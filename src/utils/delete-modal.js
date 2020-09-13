// we need our modal component
import DeleteModal from '../components/modal/DeleteModal'

const Modal = {
  // every plugin for Vue.js needs install method
  // this method will run after Vue.use(<your-plugin-here>) is executed
  // eslint-disable-next-line
  install(Vue, options) {
    // We must create new Eventbus
    // which is just another Vue instance that will be listening for and emiting events from our main instance 
    // this EventBus will be available as Modal.EventBus
    this.EventBus = new Vue()
    
    // making our modal component global
    Vue.component('delete-modal', DeleteModal)

    // exposing global $deleteModal object with method show()
    // method show() takes object params as argument
    // inside this object we can have modal title, text, styles... and also our callback confirm function
    Vue.prototype.$deleteModal = {
      show(params) {
        // if we use this.$deleteModal.show(params) inside our original Vue instance
        // we will emit 'show' event with parameters 'params'
        Modal.EventBus.$emit('show', params)
      }
    }
  }
}

export default Modal