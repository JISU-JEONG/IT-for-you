import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import VueSession from "vue-session";
import axios from "axios";

Vue.config.productionTip = false;
Vue.use(VueSession);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
