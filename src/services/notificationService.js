import api from "@/services/api";

export default {
  get_my_notifications(payload) {
    return api
      .post("get_my_notifications/", payload)
      .then(response => response.data);
  }
};
