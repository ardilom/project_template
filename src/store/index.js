import Vue from 'vue';
import Vuex from 'vuex';
import login from './modules/login';
import alert from './modules/alert';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    login,
    alert,
  },
  state: {
      user: null
  },
  mutations: {
      setAuthUser(state, user) {
          state.user = user;
      }
  },
  getters: {
      isLoggedIn(state) {
          return state.user !== null;
      }
  }
})