<template>
  <div>
    <HeaderComponent />
    <router-view ref="main" />
  </div>
</template>

<script>
import HeaderComponent from "../components/HeaderComponent";

export default {
  components: {
    HeaderComponent
  },
  methods: {
    testSocket: function() {
      // $socket is [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) instance
      // or with {format: 'json'} enabled
      this.$socket.sendObj({ message: "sending message" });
    },
  }
}
</script>