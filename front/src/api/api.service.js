import axios from "axios";
import { API_URL } from "@/api/config";

const token = JSON.parse(sessionStorage.getItem("vue-session-key"))["jwt"];
console.log(token);
export default axios.create({
  baseURL: API_URL,
  headers: {
    Authorization: `JWT ${token}`,
    "Content-type": "application/json"
  }
});
