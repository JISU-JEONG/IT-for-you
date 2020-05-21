import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    data: null,
  },

  mutations: {
    setValue(state, company) {
      state.data = company;
    },
  },
  actions: {
    questionData(context, company) {
      context.commit("setValue", company);
    },
  },
  modules: {
    auth,
  },
});
