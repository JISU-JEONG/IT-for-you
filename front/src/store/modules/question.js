import axios from "../../api/api.service";

const state = {
  questionList: null,
  questionType: null,
  questionCategory: null,
  answerList: [],
  interviewList: [],
  interviewResult: '',
  data: new FormData(),
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
  setInterviewList(state, payload) {
    state.interviewList = payload;
  },
  setInterviewResult(state, payload) {
    state.interviewResult = payload
  },
  setAudioData(state, payload) {
    state.data = payload
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
  setInterviewList(context, payload) {
    axios.post("/api/interprobs/search/", payload).then(res => {
      context.commit("setInterviewList", res.data);
    });
  }
};

const getters = {
  questionList: state => state.questionList,
  questionType: state => state.questionType,
  questionCategory: state => state.questionCategory,
  interviewList: state => state.interviewList,
  answerList: state =>
    state.questionList
      .map(q => q.answers)
      .map(q2 => q2.filter(q3 => q3.a_correct).map(q4 => q4.a_value)),
  interviewResult: state => state.interviewResult,
  interviewTag: state => [...new Set(state.interviewList.map(interview => interview.p_code))]
};

export default {
  state,
  mutations,
  actions,
  getters
};
