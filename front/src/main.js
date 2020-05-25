import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import VueSession from "vue-session";
import VueCodeHighlight from "vue-code-highlight";

Vue.config.productionTip = false;
Vue.use(VueSession);
Vue.use(VueCodeHighlight);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
