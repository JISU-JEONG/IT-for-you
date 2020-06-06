import axios from '../../api/api.service'

const state = {
  questionList: null,
  questionType: null,
  questionCategory: null,
  myNoteList: null,
  wrongAnswerList: null,
  answerList: [],
  interviewList: [],
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
  },
  setInterviewList(state, payload) {
    state.interviewList = payload
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
  myNoteList(context, values) {
    context.commit("setMyNoteList", values);
  },
  wrongAnswerList(context, values) {
    context.commit("setWrongAnswerList", values);
  },
  setInterviewList(context, payload) {
    axios.post('/api/interprobs/search/', payload)
      .then(res => {
        context.commit('setInterviewList', res.data)
      })
  }
};

const getters = {
  questionList: state => state.questionList,
  questionType: state => state.questionType,
  questionCategory: state => state.questionCategory,
  myNoteList: state => state.myNoteList,
  wrongAnswerList: state => state.wrongAnswerList,
  answerList: state =>
    state.questionList
      .map(q => q.answers)
      .map(q2 => q2.filter(q3 => q3.a_correct).map(q4 => q4.a_value))
};

export default {
  state,
  mutations,
  actions,
  getters
};
