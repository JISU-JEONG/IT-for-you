const state = {
  labels: null,
  series: null
};

const mutations = {
  setLabels(state, values) {
    state.labels = values;
  },
  setSeries(state, values) {
    state.series = values;
  }
};

const actions = {
  labels(context, values) {
    context.commit("setLabels", values);
  },
  series(context, values) {
    context.commit("setSeries", values);
  }
};

const getters = {
  series: state => state.series,
  labels: state => state.labels
};

export default {
  state,
  mutations,
  actions,
  getters
};
