import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";
import question from "./modules/question";
import chart from "./modules/chart";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    question,
    chart
  }
});
