const state = {
  questionList: null,
  questionType: null,
  questionCategory: null,
  wrongAnswerList: null,
  answerList: [],
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
  wrongAnswerList: state => state.wrongAnswerList,
  answerList: state => state.questionList.map(q => q.answers).map(q2 => q2.filter(q3 => q3.a_correct).map(q4 =>q4.a_value))
};

export default {
  state,
  mutations,
  actions,
  getters
};
