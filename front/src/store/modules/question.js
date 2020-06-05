const state = {
  questionList: null,
  questionType: null,
  questionCategory: null,
  wrongAnswerList: null
};

const mutations = {
  setQuestionList(state, values) {
    state.questionList = values;
  },
  setQuestionType(state, values) {
    state.questionType = values;
  },
  setQuestionCategory(state, values) {
    state.questionCategory = values;
  },
  setWrongAnswerList(state, values) {
    state.wrongAnswerList = values;
  }
};

const actions = {
  questionList(context, values) {
    context.commit("setQuestionList", values);
  },
  questionType(context, values) {
    context.commit("setQuestionType", values);
  },
  questionCategory(context, values) {
    context.commit("setQuestionCategory", values);
  },
  wrongAnswerList(context, values) {
    context.commit("setWrongAnswerList", values);
  }
};

const getters = {
  questionList: state => state.questionList,
  questionType: state => state.questionType,
  questionCategory: state => state.questionCategory,
  wrongAnswerList: state => state.wrongAnswerList
};

export default {
  state,
  mutations,
  actions,
  getters
};
