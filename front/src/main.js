import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import VueSession from "vue-session";
import VueCodeHighlight from "vue-code-highlight";
import AudioRecorder from 'vue-audio-recorder'

Vue.config.productionTip = false;
Vue.use(VueSession);
Vue.use(VueCodeHighlight);
Vue.use(AudioRecorder);



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
