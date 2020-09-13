import api from "@/services/api";

export default {
  authenticate_password(payload) {
    return api
      .post("authenticate/password/", payload)
      .then(response => response.data);
  },
  register(payload) {
    return api.post("register/", payload).then(response => response.data);
  }
};
