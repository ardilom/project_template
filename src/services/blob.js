import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export default axios.create({
  baseURL: "/api",
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
    Authorization: {
      toString() {
        return `Token ${localStorage.getItem("token")}`;
      }
    }
  },
  responseType: "blob"
});
