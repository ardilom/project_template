import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export default axios.create({
  baseURL: "/api",
  headers: {
    Authorization: {
      toString() {
        return `Token ${localStorage.getItem("token")}`;
      }
    }
  }
});
