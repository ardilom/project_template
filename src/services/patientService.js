import api from "@/services/api";
//import blob from "@/services/blob";

export default {
  // forms
  get_forms(payload) {
    return api.get("forms/admin/", payload).then(response => response.data);
  },
  create_patient_form(payload) {
    return api
      .post("forms/admin/", payload)
      .then(response => response.data);
  },
  send_form(payload) {
    let auth_url = payload.authenticated ? "admin" : "user"; 
    return api
      .put("forms/" + auth_url + "/" + payload.id + "/", payload)
      .then(response => response.data);
  },
  get_form(payload) {
    let auth_url = payload.authenticated ? "admin" : "user"; 
    return api
      .get("forms/" + auth_url + "/" + payload.id + "/", payload)
      .then(response => response.data);
  },
  delete_form(payload) {
    return api.delete("forms/admin/" + payload.id + "/", payload).then(response => response.data);
  },
};
