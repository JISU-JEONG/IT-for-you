const state = {
  questionData: null,
  filters: null
};

const mutations = {
  setQuestionData(state, values) {
    state.questionData = values;
  },
  setFilters(state, values) {
    state.filters = values;
  }
};

const actions = {
  questionData(context, values) {
    context.commit("setQuestionData", values);
  },
  filters(context, values) {
    context.commit("setFilters", values);
  }
};

const getters = {
  questionData: state => state.questionData,
  filters: state => state.filters
};

export default {
  state,
  mutations,
  actions,
  getters
};
