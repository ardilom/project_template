export default {
  namespaced: true,
  state: {
    token: localStorage.getItem('token'),
    first_name: localStorage.getItem('first_name'),
    last_name: localStorage.getItem('last_name'),
    email: localStorage.getItem('email'),
    thumbnail: localStorage.getItem('thumbnail'),
    notifications: [],
  },
  mutations: {
    setUser (state, payload) {
      state.token = payload.token;
      localStorage.setItem('token', payload.token);
      state.first_name = payload.first_name;
      localStorage.setItem('first_name', payload.first_name);
      state.last_name = payload.last_name;
      localStorage.setItem('last_name', payload.last_name);
      state.email = payload.email;
      localStorage.setItem('email', payload.email);
      state.thumbnail = payload.thumbnail;
      localStorage.setItem('thumbnail', payload.thumbnail);
    },
    setUserEmpty (state) {
      state.token = '';
      localStorage.setItem('token', '');
      state.first_name = '';
      localStorage.setItem('first_name', '');
      state.last_name = '';
      localStorage.setItem('last_name', '');
      state.email = '';
      localStorage.setItem('email', '');
      state.thumbnail = '';
      localStorage.setItem('thumbnail', '');
    },
    setNotifications(state, payload) {
      state.notifications = payload.notifications;
    },
    addNotification(state, payload) {
      state.notifications.unshift(payload);
    }
  }
};