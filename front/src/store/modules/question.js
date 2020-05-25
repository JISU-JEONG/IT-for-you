const state = {
  questionList: null
};

const mutations = {
  setQuestionList(state, values) {
    state.questionList = values;
  }
};

const actions = {
  questionList(context, values) {
    context.commit("setQuestionList", values);
  }
};

const getters = {
  questionList: state => state.questionList
};

export default {
  state,
  mutations,
  actions,
  getters
};
